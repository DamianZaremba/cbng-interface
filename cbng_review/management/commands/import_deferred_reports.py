from datetime import datetime

from cbng_report.models import Report, Comment
from cbng_review.models import EditGroup, Edit
from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Import deferred reports into the review interface'

    def handle(self, *args, **options):
        eg, n = EditGroup.objects.get_or_create(name='Deferred reports')
        if n:
            eg.weight = 90
            eg.save()

        # Get all know ids
        edit_ids = set(Edit.objects.filter(group=eg).exclude(report=None).values_list('report', flat=True))

        # Get all reports that aren't in the review db
        reports = Report.objects.filter(status=2).exclude(vandalism__id__in=edit_ids)

        # Create edits for all the reports above
        for report in reports:
            print('Creating edit for report %d' % report.vandalism.id)
            Edit.objects.create(
                timestamp=datetime.now(),
                user=report.vandalism.user,
                article=report.vandalism.article,
                old_id=report.vandalism.old_id,
                new_id=report.vandalism.new_id,
                group=eg,
                report=report.vandalism.id,
            )

            Comment.objects.create(vandalism=report.vandalism,
                                    timestamp=datetime.now(),
                                    user=None,
                                    comment='Review started')