from django.apps import AppConfig
from django.db.models import BigAutoField
from django.conf import settings
from django.core.mail import send_mail

class SendemailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sendemail'
