from __future__ import unicode_literals
from django.db import models
import requests
import logging
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class Beaten(models.Model):
    timestamp = models.DateTimeField()
    article = models.CharField(max_length=256)
    diff = models.CharField(max_length=512)
    user = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'beaten'


class Comment(models.Model):
    commentid = models.AutoField(primary_key=True)
    vandalism = models.OneToOneField('Vandalism',
                                     db_column='revertid',
                                     primary_key=True)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, db_column='userid', null=True, blank=True)
    comment = models.TextField()

    @property
    def id(self):
        return self.commentid

    class Meta:
        managed = False
        db_table = 'comments'


class Report(models.Model):
    STATUSES = (
        (0, 'Reported'),
        (1, 'Invalid'),
        (2, 'Defer to Review Interface'),
        (3, 'Bug'),
        (4, 'Resolved'),
    )
    vandalism = models.OneToOneField('Vandalism',
                                     db_column='revertid',
                                     primary_key=True)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, db_column='reporterid', null=True, blank=True)
    status = models.IntegerField(choices=STATUSES, default=0)

    class Meta:
        managed = False
        db_table = 'reports'


class User(models.Model):
    '''
    Deprecated - used for mapping account privileges ONLY
    '''
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
    old_id = models.IntegerField()
    new_id = models.IntegerField()
    reverted = models.IntegerField()
    _diff = None

    @property
    def diff(self):
        if not self._diff:
            try:
                r = requests.get('https://en.wikipedia.org/w/index.php',
                                 {
                                     'diffonly': 1,
                                     'action': 'render',
                                     'diff': self.new_id
                                 }, timeout=5)

                if r.status_code == 200:
                    self._diff = r.text
            except Exception as e:
                logger.error('Failed to load diff', e)
        return self._diff

    class Meta:
        managed = False
        db_table = 'vandalism'


class ClusterNode(models.Model):
    type = models.CharField(max_length=256)
    node = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'cluster_node'
