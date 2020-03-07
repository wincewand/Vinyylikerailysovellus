from django.db import models

# Create your models here.
class Albumi(models.Model):
    albumi_id = models.AutoField(primary_key=True)
    albumi_artisti = models.CharField(max_length=250)
    albumi_nimi = models.CharField(max_length=250)
    albumi_vuosi = models.CharField(max_length=250)