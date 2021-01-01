from django.db import models

# Create your models here.
# What we need: candidate name, introduction, number,
# where the candidate is running for.
# We need a class that contains such information.
# That sort of file is models.py in Django.

class Candidate(models.Model): # we need inheritance from models.Model
    name = models.CharField(max_length=10) # 길이제한
    introduction = models.TextField() # 길이제한 없음
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=1)
