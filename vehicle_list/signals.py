from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save
from .utils import unique_slug_generator_vehicle

from .models import Vehicle

from django.conf import settings

@receiver(pre_save, sender=Vehicle)
def save_product(sender, instance, *args, **kwarg):
    if not instance.slug:
        instance.slug = unique_slug_generator_vehicle(instance)