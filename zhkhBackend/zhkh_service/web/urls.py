from django.urls import path

from web.views import NewsListAPIView


urlpatterns = [
    path('news/', NewsListAPIView.as_view(), name='news-list'),
]