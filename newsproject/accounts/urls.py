from django.urls import path
from .views import AccountView, upgrade_me, subscribes

urlpatterns = [
    path('account/', AccountView.as_view()),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('subscribe/', subscribes, name='subscribe'),
]