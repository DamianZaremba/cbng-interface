from django.db import models
import logging
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class ClientClassification(models.Model):
    CLASSIFICATIONS = (
        (0, 'Vandalism'),
        (1, 'Constructive'),
        (2, 'Skipped'),
        (3, 'Unknown')
    )

    user = models.ForeignKey(User)
    comment = models.CharField(max_length=256)
    classification = models.CharField(max_length=256)
    editKey = models.CharField(max_length=256)
    edit = models.CharField(max_length=256)
