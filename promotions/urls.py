from django.urls import path
# from .views import PromotionAPIView, PromotionDetailAPIView



from .views import PromotionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'promotions', PromotionViewSet)

app_name = 'promotions'

urlpatterns = [
    # path('promotions/', PromotionAPIView.as_view()),
    # path('promotions/<int:pk>/', PromotionDetailAPIView.as_view())
] + router.urls
