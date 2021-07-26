from django.urls import path

from .views import Home, admin


urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('admin_company', admin, name='admin')
]
