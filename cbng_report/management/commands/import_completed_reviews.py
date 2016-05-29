from datetime import datetime

from cbng_report.models import Report, Comment
from cbng_review.models import Edit
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Import edits that have finished being reviewed'

    def handle(self, *args, **options):
        report_ids = set(Report.objects.filter(status=2).values_list('vandalism', flat=True).distinct())

        edits = Edit.objects.filter(status=2, report__in=report_ids)
        for edit in edits:
            print('Marking report %d complete' % edit.report)
            r = Report.objects.get(vandalism__id=edit.report)
            r.status = 4
            r.save()

            Comment.objects.create(vandalism__id=edit.report,
                                   timestamp=datetime.now(),
                                   user=None,
                                   comment='Review completed')
