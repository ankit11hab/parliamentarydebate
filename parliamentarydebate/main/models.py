import email
from unittest.util import _MAX_LENGTH
from cairo import Format
from django.db import models
from sqlalchemy import null, true

# Create your models here.

class teams(models.Model):
    POCname=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    email=models.EmailField(max_length=40,null=True)
    contactno=models.CharField(max_length=10,null=True)
    teamSlots=models.CharField(max_length=10,null=True)
    info=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.college

class adjudicators(models.Model):
    name=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    contactno=models.CharField(max_length=10,null=True)
    email=models.EmailField(max_length=40,null=True)
    info=models.CharField(max_length=100,null=True)
    TournamentName=models.CharField(max_length=100,null=True)
    Year=models.CharField(max_length=10,null=True)
    Format=models.CharField(max_length=100,null=True)
    Size=models.CharField(max_length=100,null=True)
    POB=models.CharField(max_length=100,null=True)
    OutroundSpoken=models.CharField(max_length=100,null=True)
    awards=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class crossOpen(models.Model):
    TeamName=models.CharField(max_length=100)
    Country=models.CharField(max_length=100)
    Name_of_Poc =models.CharField(max_length=100)
    contactno=models.CharField(max_length=10,null=True)
    email=models.EmailField(max_length=40,null=True)
    info=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.TeamName