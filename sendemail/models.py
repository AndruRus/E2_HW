from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
import threading


class EmailList(models.Model):
    email = models.EmailField(blank=True, null=True)
    delay = models.IntegerField()
    message = models.CharField(max_length=25)

    def __str__(self):
        return self.message


def email_yandex(message, email=''):
    send_mail(
        'Test Email',
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=True
    )


@receiver(pre_save, sender=EmailList)
def send_email(sender, instance, **kwargs):
    t = threading.Timer(instance.delay, email_yandex, args=(instance.message, instance.email, ))
    t.start()