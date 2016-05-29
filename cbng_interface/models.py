from django.db import models
import logging
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class Preferences(models.Model):
    next_on_review = models.BooleanField(help_text='Auto redirect when reviewing',
                                         default=1)
    user = models.OneToOneField(User)

    def __str__(self):
        return 'Preferences for %s' % self.user.username