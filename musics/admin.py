from django.contrib import admin
from .models import Music,Album

#admin.site.register(Music)
#admin.site.register(Album)
#from django.contrib import admin
#from .models import Music, Album

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'artiste', 'album', 'time_length', 'audio_file', 'cover_image')
    # Optionally, you can use a more detailed form view:
    fields = ('title', 'artiste', 'album', 'time_length', 'audio_file', 'cover_image')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name',)
