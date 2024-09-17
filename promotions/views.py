from rest_framework.decorators import api_view
from .models import Promotion
from .serializers.promotion_serializers import PromotionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from rest_framework.permissions import IsAuthenticated



class PromotionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class PromotionAPIView(APIView):

    def get(self, request):
        promotions = Promotion.objects.all()
        serializer = PromotionSerializer(promotions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PromotionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST)


class PromotionDetailAPIView(APIView):
    
    # Buscar uma promocao
    def get_object(self, pk):
        try:
                return Promotion.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self, request, pk):
        promotion = self.get_object(pk)
        serializer = PromotionSerializer(promotion)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    

# FUNCTION BASED VIEWS
@api_view(['GET', 'POST'])
def promotions_list(request):
    if request.method == 'GET':
        promotions = Promotion.objects.all()
        serializer = PromotionSerializer(promotions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PromotionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)

# promotions/2/

@api_view(['GET', 'PUT', 'DELETE'])
def detail_promotion(request, pk):
    try:
        promotion = Promotion.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PromotionSerializer(promotion)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = PromotionSerializer(promotion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        promotion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)