from django.db import models

class lang(models.Model):

 name= models.CharField(max_length=50)
 paradign= models.CharField(max_length=50)


