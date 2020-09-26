from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Registration
from django.core.mail import send_mail
from eventsite import settings


@receiver(post_save, sender=Registration)
def notification_of_registration(sender, instance, created, **kwargs):
    if created:
        print("Created registration")
        send_mail(
            'New Registration Created',
            'Do not forget to attend.',
            settings.REGISTRATION_EMAIL,
            [settings.REGISTRATION_EMAIL],
            fail_silently=False,
        )
