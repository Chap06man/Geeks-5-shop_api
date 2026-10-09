import os
from celery import Celery
from celery.beat import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

app = Celery("main")
app.conf.timezone = "Asia/Bishkek"

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "send_report_mail": {
        "task": "users.tasks.send_report_mail",
        "schedule": crontab(minute="*"),
    }
}

app.conf.beat_schedule = {
    "sleep_time_mail": {
        "task": "users.tasks.sleep_time_mail",
        "schedule": crontab(hour=22, minute=30)
    }
}

app.conf.beat_schedule = {
    "login_static_mail": {
        "task": "users.tasks.login_static_mail",
        "schedule": crontab(hour=00, minute=1)
    }
}