from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Create the expected groups for the CBNG interface'

    def handle(self, *args, **options):
        g, n = Group.objects.get_or_create(name='reporters')
        g.permissions.add(Permission.objects.get(codename='add_comments'))
        g.save()

        g, n = Group.objects.get_or_create(name='reviewers')
        g.permissions.add(Permission.objects.get(codename='delete_comments'))
        g.permissions.add(Permission.objects.get(codename='can_review'))
        g.permissions.add(Permission.objects.get(codename='change_reports'))
        g.save()

        g, n = Group.objects.get_or_create(name='admins')
        g.permissions.add(Permission.objects.get(codename='can_review_admin'))
        g.save()
