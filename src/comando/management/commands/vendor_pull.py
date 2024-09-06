import helpers

from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand

STATICFILES_VENDOR_DIR = getattr(settings, "STATIC_FILES_VENDOR_DIR")

VENDOR_STATIC_FILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js",
}


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Downloading vendor static files"))
        for filename, url in VENDOR_STATIC_FILES.items():
            out_path = STATICFILES_VENDOR_DIR / filename
            dl_success = helpers.download_to_local(url, out_path)
            if dl_success:
                self.stdout.write(self.style.SUCCESS(f"Downloaded {filename}"))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to download {filename}"))