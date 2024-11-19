from rest_framework.serializers import ModelSerializer

from web.models import News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'description', 'image', 'date_created')