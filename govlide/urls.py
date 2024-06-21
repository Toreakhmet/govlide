
from django.contrib import admin
from django.urls import path
from main_page.views import home,send_email
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name='home'),
    path("send_email",send_email,name='forms')
]
