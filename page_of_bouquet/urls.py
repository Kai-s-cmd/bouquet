from django.urls import path
from .views import HomePageView, ThanksPageView, send_email


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('thanks/', ThanksPageView.as_view(), name='thanks'),
    path('send-email/', send_email, name='send_email'),
]