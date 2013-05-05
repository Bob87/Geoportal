from django.db import models

class Metadatabase(models.Model):
    uuid        = models.IntegerField()
    schemaid    = models.CharField(max_length=32)
    istemplate  = models.CharField(max_length=1)
    isharvested = models.CharField(max_length=1)
    createdate  = models.CharField(max_length=24)
    changedate  = models.CharField(max_length=24)
    data        = models.CharField(max_length=255) #text
    source      = models.CharField(max_length=250)
    title       = models.CharField(max_length=255)
    root        = models.CharField(max_length=255)
    harvestuuid = models.CharField(max_length=250)
    owner       = models.IntegerField()
    groupowner  = models.IntegerField()
    harvesturi  = models.CharField(max_length=255)
    rating      = models.IntegerField()
    popularity  = models.IntegerField()
    displayorder= models.IntegerField()
