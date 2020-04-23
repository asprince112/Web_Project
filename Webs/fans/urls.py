from django.urls import path
from fans import views

app_name = 'fans'

urlpatterns = [
    path('', views.FansHome.as_view(), name='fans_home'),
    path('Miller/', views.MillerHome.as_view(), name='miller'),
    path('Oscar/', views.OscarHome.as_view(), name='oscar'),
    path('Sam/', views.SamHome.as_view(), name='sam'),
    path('William/', views.WilliamHome.as_view(), name='william'),
    path('Kobe/', views.KobeHome.as_view(), name='kobe'),
    path('Tim/', views.TimHome.as_view(), name='tim'),

]
