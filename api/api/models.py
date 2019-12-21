from django.db import models
from django.db.models import CASCADE


class Person(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)


class Allocation(models.Model):
    person = models.ForeignKey(Person, on_delete=CASCADE)
    project = models.ForeignKey(Project, on_delete=CASCADE)
    schedule_start = models.DateTimeField()
    schedule_stop = models.DateTimeField()
    start = models.DateTimeField()
    stop = models.DateTimeField()