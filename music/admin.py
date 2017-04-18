from django.contrib import admin


from .models import Album
from .models import Song
# Register your models here.

# Add album into admin site
admin.site.register(Album)
admin.site.register(Song)
