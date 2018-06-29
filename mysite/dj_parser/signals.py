from django.db.models.signals import post_save
from django.dispatch import receiver

from dj_parser.models import Page
from dj_parser.tasks import parse_page


@receiver(post_save, sender=Page)
def parse_in_celery(sender, instance, created, **kwargs):
    if created:
        parse_page.delay(instance.id)