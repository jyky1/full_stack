import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_api.settings')
app = Celery('main_api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()