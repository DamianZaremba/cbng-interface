import logging

import requests
from django.contrib.auth.models import User
from django.db import models

logger = logging.getLogger(__name__)


class EditGroup(models.Model):
    name = models.CharField(max_length=256)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Edit(models.Model):
    STATUSES = (
        (0, 'Not Done'),
        (1, 'Partially Done'),
        (2, 'Done')
    )

    CLASSIFICATION_UNKNOWN = 0
    CLASSIFICATION_VANDALISM = 1
    CLASSIFICATION_CONSTRUCTIVE = 2
    CLASSIFICATION_SKIPPED = 3

    timestamp = models.DateTimeField()
    user = models.CharField(max_length=256)
    article = models.CharField(max_length=256)
    old_id = models.IntegerField()
    new_id = models.IntegerField()
    required = models.IntegerField(default=2)
    group = models.ForeignKey(EditGroup)
    report = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(choices=STATUSES, default=0)
    _diff = None

    def __str__(self):
        return '<Edit:%d>' % self.id

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

    def recalculate_status(self):
        constructive = Classification.objects.filter(edit=self,
                                                     classification=1).count()
        vandalism = Classification.objects.filter(edit=self,
                                                  classification=0).count()
        skipped = Classification.objects.filter(edit=self,
                                                classification=2).count()

        sum = constructive + vandalism + skipped
        maxc = max(constructive, max(vandalism, skipped))

        if sum == 0:
            self.status = 0
        else:
            if maxc > self.required and self.classification != self.CLASSIFICATION_UNKNOWN:
                self.status = 2
            else:
                self.status = 1
        self.save()

    @property
    def classification(self):
        constructive = Classification.objects.filter(edit=self,
                                                     classification=1).count()
        vandalism = Classification.objects.filter(edit=self,
                                                  classification=0).count()
        skipped = Classification.objects.filter(edit=self,
                                                classification=2).count()

        sum = constructive + vandalism + skipped
        maxc = max(constructive, max(vandalism, skipped))

        if maxc > self.required:
            if (2 * skipped) > sum:
                return self.CLASSIFICATION_SKIPPED

            if constructive >= (3 * vandalism):
                return self.CLASSIFICATION_CONSTRUCTIVE

            if vandalism >= (3 * constructive):
                return self.CLASSIFICATION_VANDALISM

        return self.CLASSIFICATION_UNKNOWN

    class Meta:
        permissions = (
            ('can_review', 'Can review edits'),
            ('can_review_admin', 'Can review edits'),
        )


class Classification(models.Model):
    CLASSIFICATIONS = (
        (0, 'Vandalism'),
        (1, 'Constructive'),
        (2, 'Skipped')
    )

    user = models.ForeignKey(User)
    comment = models.CharField(max_length=256, blank=True, null=True)
    classification = models.IntegerField(choices=CLASSIFICATIONS)
    edit = models.ForeignKey(Edit)

    def __str__(self):
        return '<Classification:%d>' % self.id

    def save(self, *args, **kwargs):
        super(Classification, self).save(*args, **kwargs)

        # Check if this edit is done
        self.edit.recalculate_status()

    class Meta:
        unique_together = (('user', 'edit'),)


class UserAccessRequest(models.Model):
    user = models.OneToOneField(User)
    processed = models.BooleanField(default=False)
    comment = models.TextField()

    def __str__(self):
        return '<UserAccessRequest:%d>' % self.id
