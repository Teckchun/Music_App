from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy



"""

Always run
1. python manage.py makemigrations model_name
2. python manage.py migrate

whenever you have sth change in your model


"""


# Django will automatically create primary key for our model
# Create your models here.

class Album(models.Model):

    #creating model field

    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    #album_logo = models.CharField(max_length=1000)
    album_logo = models.FileField()


    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})


    #create to string function

    def __str__(self):
        return self.album_title + ' - ' + self.artist

# each song is gonna be link to an album
class Song(models.Model):
    # create relationship
    album = models.ForeignKey(Album, on_delete=models.CASCADE) # when the album is delete, songs inside that one will also be deleted
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.song_title



