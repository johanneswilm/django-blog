from django.core.management.base import BaseCommand, CommandError
from blog.models import UserImages


class Command(BaseCommand):
    help = "Calculates the modified images"

    def handle(self, *args, **options):
        for image in UserImages.objects.filter(modified_file__isnull=True).iterator():
            image.calculate_modified_file()

        self.stdout.write(self.style.SUCCESS("Successfully stored modified files"))
