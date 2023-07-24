from django.core.management.base import BaseCommand
from accounts.models import Work

class Command(BaseCommand):
    help = 'Adds dummy data to the Work model for testing API calls.'

    def handle(self, *args, **kwargs):
        # Create dummy data for Work model
        Work.objects.create(link='https://www.youtube.com/dummy1', work_type='YT')
        Work.objects.create(link='https://www.instagram.com/dummy2', work_type='IG')
        Work.objects.create(link='https://www.example.com/dummy3', work_type='OT')

        self.stdout.write(self.style.SUCCESS('Dummy data added successfully.'))
