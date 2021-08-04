from django.urls import path, include, re_path

from .views import *


urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', user_logout, name='logout'),
    path('admin_company/', admin_company, name='admin_company'),
    path('create_customer_form/', create_customer_form),
    path('register/', Register.as_view(), name='register')
]
