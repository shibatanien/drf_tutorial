from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Drink
from .serializers import DrinkSerializer

class DrinkList(APIView):
    def get(self, request, format=None):
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = DrinkSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DrinkDetail(APIView):
    def get_object(self, pk):
        try:
            return Drink.objects.get(pk=pk)
        except Drink.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        drink = self.get_object(pk)
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        drink = self.get_object(pk)
        serializer = DrinkSerializer(drink, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        drink = self.get_object(pk)
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
