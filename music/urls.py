from django.conf.urls import url
from . import views   # from . mean looking in side this directory

app_name = 'music'  # use this to determine which url in which app should be called

urlpatterns = [
    # setting index for each individual app
    #/music/
    #url(r'^$', views.index, name='index'),

    url(r'^$',views.IndexView.as_view(), name='index'),
    #/music/1/
    # url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),

   #using generic view
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

   #Todo: AlbumCreate url
   #/music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

   #Todo: AlbumUpdate url
   # /music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

   # Todo: AlbumDelete url
   # /music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    #Todo: User registration
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

]
