
from djongo import models

# Create your models here.

class Album(models.Model):
    name = models.TextField()
    artist = models.TextField()
    year = models.IntegerField()
    user = models.TextField()
    _id = models.ObjectIdField()

    # def __str__(self):
    #     return self.name

class Meta:
        managed = False
        db_table = 'Album'