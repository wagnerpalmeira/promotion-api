from django.urls import path
from .views import promotions_list, detail_promotion

app_name = 'promotions'

urlpatterns = [
    path('promotions/', promotions_list),
    path('promotions/<int:pk>/', detail_promotion)
]
