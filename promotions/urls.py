from django.urls import path
from .views import PromotionAPIView, PromotionDetailAPIView

app_name = 'promotions'

urlpatterns = [
    path('promotions/', PromotionAPIView.as_view()),
    path('promotions/<int:pk>/', PromotionDetailAPIView.as_view())
]
