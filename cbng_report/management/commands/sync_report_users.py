from cbng_report.models import Report, Comment
from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Sync comments/reports to known users'

    def handle(self, *args, **options):
        # Get known users
        users = {}
        for user in User.objects.all():
            users[user.username] = user.id

        for report in Report.objects.filter(reporter__in=users.keys()):
            if report.user_id != users[report.reporter]:
                print('Updating user association for report %d' % report.id)
                report.user_id = users[report.reporter]
                report.save()

        for comment in Comment.objects.filter(commenter__in=users.keys()):
            if comment.user_id != users[comment.commenter]:
                print('Updating user association for comment %d' % comment.id)
                comment.user_id = users[comment.commenter]
                comment.save()
