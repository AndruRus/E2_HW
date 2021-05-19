
from django.contrib import admin
from django.urls import path
from sendemail.views import MainView, SendsView, EmailListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('sends/', SendsView.as_view(), name='sends'),
    path('list/', EmailListView.as_view(), name='list'),
]
