from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.strona_glowna, name='strona_glowna'),
    path('lot/<int:lot_id>', views.lot, name='lot'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
]
