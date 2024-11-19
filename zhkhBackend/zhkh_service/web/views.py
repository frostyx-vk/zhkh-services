from django.conf import settings
from django.contrib.auth.views import PasswordResetCompleteView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from web.models import News
from web.serializers import NewsSerializer


class PasswordResetCompleteCustomView(PasswordResetCompleteView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_url"] = settings.FRONTEND_LINK
        return context


class NewsListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NewsSerializer
    queryset = News.objects.all()