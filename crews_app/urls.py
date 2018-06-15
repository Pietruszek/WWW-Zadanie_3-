from django.urls import path
from . import views

urlpatterns = [
    path('zalogi/', views.zalogi, name='zalogi'),
    path('rest/zalogi/', views.rest_zalogi, name='rest_zalogi'),
    path('rest/loty/<str:data>/', views.rest_loty, name='rest_loty'),
    path('rest/zaloga_lotu/', views.rest_zmiana_zalogi, name='rest_zmiana_zalogi')
]
