from django.core.management.base import BaseCommand
from cbng_legacy_report.models import Reports


class Command(BaseCommand):
    help = 'Syncs old report entries to the new report structure'

    def handle(self, *args, **options):
        for report in Reports.objects.all():
            print report.revertid.id

            break
