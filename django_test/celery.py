import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_test.settings")
app = Celery("django_test", broker="redis://localhost:6379")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
