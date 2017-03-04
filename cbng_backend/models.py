import requests
from django.db import models
import logging

logger = logging.getLogger(__name__)


class ClusterNode(models.Model):
    type = models.CharField(max_length=256)
    node = models.CharField(max_length=256)

    class Meta:
        managed = False


class Vandalism(models.Model):
    timestamp = models.DateTimeField()
    user = models.CharField(max_length=256)
    article = models.CharField(max_length=256)
    heuristic = models.CharField(max_length=64)
    reason = models.CharField(max_length=512)
    diff = models.CharField(max_length=512)
    old_id = models.IntegerField()
    new_id = models.IntegerField()
    reverted = models.IntegerField()
    _diff = None

    def get_diff(self):
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
        db_table = 'vandalism'
        managed = False


class Beaten(models.Model):
    timestamp = models.DateTimeField()
    article = models.CharField(max_length=256)
    diff = models.CharField(max_length=512)
    user = models.CharField(max_length=256)

    class Meta:
        db_table = 'beaten'
        managed = False
