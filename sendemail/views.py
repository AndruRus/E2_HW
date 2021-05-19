from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic import CreateView, ListView
from sendemail.forms import ContactForm
from sendemail.models import EmailList
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail


class SendsView(TemplateView):

    template_name = 'sends.html'


class MainView(CreateView):
    model = EmailList
    form_class = ContactForm
    success_url = reverse_lazy('sends')
    template_name = 'main.html'  


class EmailListView(ListView):

    model = EmailList


    def get_queryset(self):
        context = EmailList.objects.order_by('-pk')[:10]
        return context
