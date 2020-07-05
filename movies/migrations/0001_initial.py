# Generated by Django 3.0.6 on 2020-06-15 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionRealMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('season', models.CharField(blank=True, max_length=220)),
                ('subtitle', models.CharField(blank=True, max_length=220)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('embed', models.CharField(blank=True, help_text='Domain embed code', max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=1500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ActionThrillerMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('season', models.CharField(blank=True, max_length=220)),
                ('subtitle', models.CharField(blank=True, max_length=220)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('embed', models.CharField(blank=True, help_text='Domain embed code', max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=1500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AdventureRealMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('season', models.CharField(blank=True, max_length=220)),
                ('subtitle', models.CharField(blank=True, max_length=220)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('embed', models.CharField(blank=True, help_text='Domain embed code', max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=1500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AdventureThrillerMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('season', models.CharField(blank=True, max_length=220)),
                ('subtitle', models.CharField(blank=True, max_length=220)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('embed', models.CharField(blank=True, help_text='Domain embed code', max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=1500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ComedyRealMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('season', models.CharField(blank=True, max_length=220)),
                ('subtitle', models.CharField(blank=True, max_length=220)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('embed', models.CharField(blank=True, help_text='Domain embed code', max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=1500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ComedyThrillerMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('season', models.CharField(blank=True, max_length=220)),
                ('subtitle', models.CharField(blank=True, max_length=220)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('embed', models.CharField(blank=True, help_text='Domain embed code', max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=1500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DramaRealMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('season', models.CharField(blank=True, max_length=220)),
                ('subtitle', models.CharField(blank=True, max_length=220)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('embed', models.CharField(blank=True, help_text='Domain embed code', max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=1500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DramaThrillerMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('season', models.CharField(blank=True, max_length=220)),
                ('subtitle', models.CharField(blank=True, max_length=220)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('embed', models.CharField(blank=True, help_text='Domain embed code', max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=1500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FictionRealMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('season', models.CharField(blank=True, max_length=220)),
                ('subtitle', models.CharField(blank=True, max_length=220)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('embed', models.CharField(blank=True, help_text='Domain embed code', max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=1500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FictionThrillerMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('season', models.CharField(blank=True, max_length=220)),
                ('subtitle', models.CharField(blank=True, max_length=220)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('embed', models.CharField(blank=True, help_text='Domain embed code', max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=1500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalRealMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('season', models.CharField(blank=True, max_length=220)),
                ('subtitle', models.CharField(blank=True, max_length=220)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('embed', models.CharField(blank=True, help_text='Domain embed code', max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=1500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalThrillerMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('season', models.CharField(blank=True, max_length=220)),
                ('subtitle', models.CharField(blank=True, max_length=220)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('embed', models.CharField(blank=True, help_text='Domain embed code', max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=1500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
