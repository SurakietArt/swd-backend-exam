import logging
import os

from django.core import management
from django.core.management.base import BaseCommand
from django.db import IntegrityError

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Load generated school data fixtures only"
    seed_data = "seed_data"

    def handle(self, *args, **options) -> None:
        if not os.path.exists(self.seed_data):
            logger.error(f"Directory not found: {self.seed_data}")
            return

        for filename in sorted(os.listdir(self.seed_data)):
            if filename.endswith(".json"):
                filepath = os.path.join(self.seed_data, filename)
                try:
                    logger.info(f"Installing: {filepath}")
                    management.call_command("loaddata", filepath)
                except IntegrityError as e:
                    logger.warning(e)
                    logger.warning(f"Unable to install {filename}. Skipping.")
