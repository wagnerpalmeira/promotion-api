from django.urls import path
from .views import promotions_list

app_name = 'promotions'

urlpatterns = [
    path('promotions/', promotions_list)
]
