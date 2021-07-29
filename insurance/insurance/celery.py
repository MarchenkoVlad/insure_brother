""" 
    Файл настроек Celery
"""
from __future__ import absolute_import
import os
from celery import Celery
from django.core.mail import send_mail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insurance.settings')

app = Celery("insurance")


# Для получения настроек Django, связываем префикс "CELERY" с настройкой celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# загрузка tasks.py в приложение django
app.autodiscover_tasks()

@app.task
def add(x, y):
    return x / y

@app.task
def send_task_email(subject, message, email_from, recipient_list):
    send_mail(subject, message, email_from, recipient_list)
