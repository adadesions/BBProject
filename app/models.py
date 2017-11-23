""" Models for app """
from django.db import models


class Agenda(models.Model):
    """ Agenda model """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    body = models.TextField()
    img_path = models.CharField(
        max_length=256,
        default="/static/img/blog/default.jpg"
        )

    def __str__(self):
        return self.title
