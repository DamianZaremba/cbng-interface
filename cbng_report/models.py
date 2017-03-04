from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from cbng_backend.models import Vandalism


class Comment(models.Model):
    commentid = models.PositiveIntegerField(primary_key=True)
    vandalism = models.OneToOneField(Vandalism, db_column='revertid')
    timestamp = models.DateTimeField()
    userid = models.IntegerField()
    user = models.CharField(max_length=127)
    comment = models.TextField()

    class Meta:
        db_table = 'comments'
        managed = False


class Report(models.Model):
    STATUSES = (
        (0, 'Reported'),
        (1, 'Invalid'),
        (2, 'Defer to Review Interface'),
        (3, 'Bug'),
        (4, 'Resolved'),
    )
    vandalism = models.OneToOneField(Vandalism,
                                     primary_key=True,
                                     db_column='revertid')
    timestamp = models.DateTimeField()
    user = models.ForeignKey(
        User, null=True, blank=True, db_column='reporterid')
    reporter = models.CharField(max_length=128)
    status = models.IntegerField(choices=STATUSES, default=0)

    class Meta:
        db_table = 'reports'
        managed = False
