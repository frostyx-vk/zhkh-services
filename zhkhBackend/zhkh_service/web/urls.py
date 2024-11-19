from django.urls import path

from web.views import NewsListAPIView, ServiceAPIView

app_name = 'web'

urlpatterns = [
    path('news/', NewsListAPIView.as_view(), name='news-list'),
    path('services/', ServiceAPIView.as_view(), name='service-list'),
]