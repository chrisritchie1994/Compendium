from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.


class Journal(models.Model):
    journal_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    entry = models.TextField()
    rating = models.IntegerField(default=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_types = (
        ("Real", "Real"),
        ("Test", "Test")
    )
    data_type = models.CharField(
        max_length=4,
        choices=data_types,
        default="Real"
    )

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

    def r13(self):
        num = random.randint(1,3)
        if num == 1:
            return "one"
        elif num == 2:
            return "two"
        else:
            return"three"


class Aphorism(models.Model):
    aphorism_id = models.AutoField(primary_key=True)
    entry = models.TextField()
    aphorism = models.TextField()
    application = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.aphorism




class Subentry(models.Model):
    subentries_id = models.AutoField(primary_key=True)
    record_type = models.CharField(max_length=10)
    open_tag = models.CharField(max_length=10)
    close_tag =models.CharField(max_length=10)

