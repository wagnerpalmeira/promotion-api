from rest_framework import serializers
from ..models.promotion import Promotion

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'
