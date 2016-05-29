from django.core.management import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Create the expected groups for the CBNG interface'

    def handle(self, *args, **options):
        g, n = Group.objects.get_or_create(name='reporters')
        g.save()

        g, n = Group.objects.get_or_create(name='reviewers')
        g.save()

        g, n = Group.objects.get_or_create(name='admins')
        g.save()
