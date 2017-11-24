""" Models for app """
from django.db import models
from django.utils import timezone


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
        return '%s %s' % (self.id, self.date)


class Applicant(models.Model):
    """ Applicant Model """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    recommender = models.CharField(max_length=128)
    reason = models.TextField()
    address = models.TextField()
    date = models.DateField(timezone.now())
    time = models.TimeField(timezone.now())

    def __str__(self):
        return '%s %s %s' % (self.id, self.name, self.date)
