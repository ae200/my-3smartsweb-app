from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from actionreal.mixins import  MemberRequiredMixin
from accounts.accountapi.views import  UserViewSet 
from accounts.accountapi.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from actionreal.models import ActionRealMovie

# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permission import IsAuthenticated

from .serializers import ActionRealMovieSerializer, ActionRealMovieDetailSerializer



class ActionRealMovieList(generics.ListAPIView):
    queryset                = ActionRealMovie.objects.all()
    serializer_class        = ActionRealMovieSerializer
    permission_classes      = []
    authentication_classes  = []
    # authentication_classes  = (TokenAuthentication,)  
    # permission_classes  = (IsAuthenticated,)


    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
           #qs = Movie.objects.filter(name__icontains=query)
           qs = ActionRealMovie.objects.search(query)
        else:
           qs = ActionRealMovie.objects.all()
        return qs 
     


class ActionRealMovieDetail(MemberRequiredMixin, generics.RetrieveAPIView):
    serializer_class        = ActionRealMovieDetailSerializer
    lookup_field            = 'slug'
    permission_classes      = []
    authentication_classes  = []     
        


    def get_queryset(self):
        return ActionRealMovie.objects.all()


class ActionRealMovieFeatured(generics.ListAPIView):
    serializer_class        = ActionRealMovieSerializer
    permission_classes      = []
    authentication_classes  = []  

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
           qs = ActionRealMovie.objects.featured().search(query)
        else:   
           qs = ActionRealMovie.objects.featured()
        return qs    

