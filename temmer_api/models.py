from django.contrib.postgres.fields import JSONField
from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=64, null=False)
    pword = models.TextField(max_length=256, null=False)


class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=32, unique=True, null=False)
    description = models.TextField(max_length=4096)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User)


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=128, null=False)
    description = models.TextField(max_length=4096)
    deadline = models.DateTimeField()
    message_history = JSONField()

    executor = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)