from djongo import models

# Create your models here.

class User(models.Model):
    email = models.TextField()
    password = models.TextField()
    _id = models.ObjectIdField()



class Meta:
        managed = False
        db_table = 'User'