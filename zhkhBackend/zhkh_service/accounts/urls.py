from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.http import JsonResponse
from django.urls import path

from accounts.views import ProfileDetailAPIView

app_name = 'accounts'


urlpatterns = [
    path('password/reset/confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]