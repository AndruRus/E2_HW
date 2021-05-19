from django.contrib import admin
from sendemail.models import EmailList
from django.conf import settings
from django.core.mail import send_mail


@admin.register(EmailList)
class EmailAdmin(admin.ModelAdmin):
    pass