from django.contrib.auth.models import User
from django.db import connections
from cbng_backend.models import Vandalism
from cbng_report.models import Report, Comment
from django.core.management import BaseCommand
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Import reports from the legacy database'

    def handle(self, *args, **options):
        # Import any vandalism we don't know about
        with connections['legacy'].cursor() as c:
            c.execute('''select
              id,
              timestamp,
              user,
              article,
              heuristic,
              reason,
              old_id,
              new_id,
              reverted from vandalism''''')

            for row in c.fetchall():
                try:
                    Vandalism.objects.get(id=row[0])
                except Vandalism.DoesNotExist:
                    Vandalism.objects.create(
                        id=row[0],
                        timestamp=row[1],
                        user=row[2],
                        article=row[3],
                        heuristic=row[4],
                        reason=row[5],
                        old_id=row[6],
                        new_id=row[7],
                        reverted=row[8]
                    )

        # Import any reports we don't know about
        with connections['legacy'].cursor() as c:
            c.execute(
                'select revertid, timestamp, reporter, status from reports')
            for row in c.fetchall():
                try:
                    v = Vandalism.objects.get(id=row[0])
                except Vandalism.DoesNotExist:
                    logger.warning(
                        'Dropping report due to missing vandalism: %d' % row[0])
                    continue

                try:
                    Report.objects.get(vandalism=v)
                except Report.DoesNotExist:
                    try:
                        u = User.objects.get(username=row[2])
                    except User.DoesNotExist:
                        u = None

                    r = Report.objects.create(vandalism=Vandalism.objects.get(id=row[0]),
                                              timestamp=row[1],
                                              user=u,
                                              status=row[3])

                    c.execute(
                        'select timestamp, user, comment from comments where revertid = %d' % row[0])
                    for row in c.fetchall():
                        try:
                            u = User.objects.get(username=row[1])
                        except User.DoesNotExist:
                            u = None

                        Comment.objects.create(vandalism=r,
                                               timestamp=row[0],
                                               user=u)
