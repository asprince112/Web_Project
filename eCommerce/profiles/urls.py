from django.urls import path
from.views import item_list, check_out

app_name = 'profiles'

urlpatterns = [
    path('', item_list, name='item_list'),
    path('check_out/', check_out, name='check_out'),
]
