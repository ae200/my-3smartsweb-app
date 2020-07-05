"""tryangular URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.urls import include, re_path
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.contrib import admin 
from django.views.generic.base import TemplateView
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('register/', register),
    # url (r'^$', TemplateView.as_view(template_name="ang_home.html"), name='home'),
    path('api/movies/', include('movies.api.urls')),
    # path('streamapi/streammovies/', include('streammovies.streamapi.urls')),
    path('actionapi/actionmovies/', include('actionmovies.actionapi.urls')),
    path('actionthrillerapi/actionthriller/', include('actionthriller.actionthrillerapi.urls')),
    path('actionrealapi/actionreal/', include('actionreal.actionrealapi.urls')),
    path('adventureapi/adventuremovies/', include('adventuremovies.adventureapi.urls')),
    path('adventurethrillerapi/adventurethriller/', include('adventurethriller.adventurethrillerapi.urls')),
    path('adventurerealapi/adventurereal/', include('adventurereal.adventurerealapi.urls')),
    path('comedyapi/comedymovies/', include('comedymovies.comedyapi.urls')),
    path('comedythrillerapi/comedythriller/', include('comedythriller.comedythrillerapi.urls')),
    path('comedyrealapi/comedyreal/', include('comedyreal.comedyrealapi.urls')),
    path('dramathrillerapi/dramathriller/', include('dramathriller.dramathrillerapi.urls')),
    path('dramarealapi/dramareal/', include('dramareal.dramarealapi.urls')),
    path('dramaapi/dramamovies/', include('dramamovies.dramaapi.urls')),
    path('fictionthrillerapi/fictionthriller/', include('fictionthriller.fictionthrillerapi.urls')),
    path('fictionrealapi/fictionreal/', include('fictionreal.fictionrealapi.urls')),
    path('fictionapi/fictionmovies/', include('fictionmovies.fictionapi.urls')),
    path('historicalapi/historicalmovies/', include('historicalmovies.historicalapi.urls')),
    path('historicalthrillerapi/historicalthriller/', include('historicalthriller.historicalthrillerapi.urls')),
    path('historicalrealapi/historicalreal/', include('historicalreal.historicalrealapi.urls')),
    # path('streamactionapi/streamactionmovies/', include('streamactionmovies.streamactionapi.urls')),
    # path('streamadventureapi/streamadventuremovies/', include('streamadventuremovies.streamadventureapi.urls')),
    # path('streamcomedyapi/streamcomedymovies/', include('streamcomedymovies.streamcomedyapi.urls')),
    # path('streamdramaapi/streamdramamovies/', include('streamdramamovies.streamdramaapi.urls')),
    # path('streamfictionapi/streamfictionmovies/', include('streamfictionmovies.streamfictionapi.urls')),
    # path('streamhistoricalapi/streamhistoricalmovies/', include('streamhistoricalmovies.streamhistoricalapi.urls')),
    path('accountapi/', include('accounts.accountapi.urls')),
    #path('accountapi/auth/', include('accounts.accountapi.urls', namespace='api-auth')),
    #path('api/user', include('accounts.api.user.urls', namespace='api-user')),
    #path('api/', include('profiles.urls', namespace='profiles')),
    # url(r'^api/status/', include('status.api.urls', namespace='api-status')),
    # url(r'^api/updates/', include('updates.api.urls')),
    path('accountapi/auth/', obtain_auth_token), 
]


urlpatterns += [
    re_path(r'^(?P<path>.*)', TemplateView.as_view(template_name="ang_movies.html"), name='movies'),
    re_path(r'^(?P<path>.*)', TemplateView.as_view(template_name="ang_home.html"), name='home'),
]
