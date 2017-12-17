from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year_of_release = models.CharField(max_length=50)
    image = models.CharField(max_length=1000)


    def __str__(self):
        return self.artist + '--' + self.genre + '--' + self.year_of_release + '--' + self.image


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)
    is_favourite = models.BooleanField(default=False)



    def __str__(self):
        return self.song_title
