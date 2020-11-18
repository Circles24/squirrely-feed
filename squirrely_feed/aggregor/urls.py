from django.urls import path
from .views import get_articles
from .tasks import aggregate_news

aggregate_news.delay()

urlpatterns = [
        path('articles', get_articles, name='get articles'),
        ]
