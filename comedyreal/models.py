from django.db import models

from django.db.models import Q
from django.db.models.signals import pre_save

from .utils import unique_slug_generator


class ComedyRealMovieQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)

    def search(self, query):
        return self.filter(
            Q(name__icontains=query) |
            Q(slug__icontains=query) |
            Q(embed__icontains=query)

        )


class ComedyRealMovieManager(models.Manager):
    def get_queryset(self):
        return ComedyRealMovieQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured().active()

    def search(self, query):
        return self.get_queryset().search(query).active()

# Create your models here.


class ComedyRealMovie(models.Model):
    name = models.CharField(max_length=220)
    season = models.CharField(max_length=220, blank=True)
    subtitle = models.CharField(max_length=220, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    embed = models.CharField(
        max_length=120,
        help_text='Domain embed code',
        null=True,
        blank=True)
    free = models.BooleanField(default=False)
    member_required = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    description = models.CharField(max_length=1500)
    timestamp = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    objects = ComedyRealMovieManager()

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

    def comedyrealmovie_pre_save_receiver(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)


pre_save.connect(ComedyRealMovie.comedyrealmovie_pre_save_receiver, sender=ComedyRealMovie)
