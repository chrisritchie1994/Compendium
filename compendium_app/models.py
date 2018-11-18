from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Journal(models.Model):
    journal_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    entry = models.TextField()
    rating = models.IntegerField(default=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Idea(models.Model):
    idea_id = models.AutoField(primary_key=True)
    entry = models.TextField()
    idea = models.TextField()
    application = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.idea


class Decision(models.Model):
    decision_id = models.AutoField(primary_key=True)
    entry = models.TextField()
    decision = models.TextField()
    application = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.decision


class Principle(models.Model):
    principle_id = models.AutoField(primary_key=True)
    entry = models.TextField()
    principle = models.TextField()
    application = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.principle


class Aphorism(models.Model):
    aphorism_id = models.AutoField(primary_key=True)
    entry = models.TextField()
    aphorism = models.TextField()
    application = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.aphorism



