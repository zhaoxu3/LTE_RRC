#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:eden.zhao //coding at 2019_03_20


from django.db import models

# Create your models here.
class IeData(models.Model):
    ie_data_id = models.AutoField(primary_key=True)
    ap_name = models.CharField(max_length=30)
    phy_type = models.CharField(max_length=11)
    ie_beacon = models.CharField(max_length=500)
    ie_probe = models.CharField(max_length=500)
    ie_auth = models.CharField(max_length=500)
    ie_assoc = models.CharField(max_length=500)
    class Meta:
        managed = False
        db_table = 'ie_data'

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
