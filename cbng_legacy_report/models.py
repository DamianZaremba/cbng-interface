from __future__ import unicode_literals
from django.db import models


class Beaten(models.Model):
    timestamp = models.DateTimeField()
    article = models.CharField(max_length=256)
    diff = models.CharField(max_length=512)
    user = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'beaten'


class Comments(models.Model):
    commentid = models.AutoField(primary_key=True)
    revertid = models.IntegerField()
    timestamp = models.DateTimeField()
    userid = models.IntegerField()
    user = models.CharField(max_length=128)
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'comments'


class Reports(models.Model):
    revertid = models.OneToOneField('Vandalism', db_column='revertid', primary_key=True)
    timestamp = models.DateTimeField()
    reporterid = models.IntegerField()
    reporter = models.CharField(max_length=128)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reports'


class Trr(models.Model):
    timestamp = models.DateTimeField()
    user = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=512)
    revid = models.IntegerField()
    md5 = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trr'


class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    admin = models.IntegerField()
    superadmin = models.IntegerField()
    next_on_review = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Vandalism(models.Model):
    timestamp = models.DateTimeField()
    user = models.CharField(max_length=256)
    article = models.CharField(max_length=256)
    heuristic = models.CharField(max_length=64)
    regex = models.CharField(max_length=2048, blank=True, null=True)
    reason = models.CharField(max_length=512)
    diff = models.CharField(max_length=512)
    old_id = models.IntegerField()
    new_id = models.IntegerField()
    reverted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vandalism'
