from rest_framework.serializers import ModelSerializer

from web.models import News, Service


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'description', 'image', 'date_created')


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ('title', 'description', 'price', 'order')