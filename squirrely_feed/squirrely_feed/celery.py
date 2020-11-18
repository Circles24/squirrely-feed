import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'squirrely_feed.settings')
app = Celery('squirrely_feed')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'aggregate-news-every-30-mins': {
        'task': 'aggregor.tasks.aggregate_news',
        'schedule': 60.0*2,
    },
}
app.autodiscover_tasks()
