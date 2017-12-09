from django.db import models

class pokemon(models.Model):

    title = models.CharField(max_length=120)

