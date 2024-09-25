from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from django.shortcuts import render
from .models import Firstbackend
from .serializers import FirstbackendSerializer

class FirstbackendAPIView(APIView):
    queryset = Firstbackend.objects.all()
    serializer_class = FirstbackendSerializer

    def get(self, request, pk=None):
        if pk:
            try:
                item = Firstbackend.objects.get(pk=pk)
            except Firstbackend.DoesNotExist:
                return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = FirstbackendSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            items = Firstbackend.objects.all()
            serializer = FirstbackendSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(
        operation_description="Получить список всех элементов",
        responses={200: FirstbackendSerializer(many=True)}
    )

    def post(self, request):
        serializer = FirstbackendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'post': serializer.date}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Получить список всех элементов",
        responses={200: FirstbackendSerializer(many=True)}
    )

    def put(self, request, pk=None):
        try:
            item = Firstbackend.objects.get(pk=pk)
        except Firstbackend.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FirstbackendSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        try:
            item = Firstbackend.objects.get(pk=pk)
        except Firstbackend.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FirstbackendSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Получить список всех элементов",
        responses={200: FirstbackendSerializer(many=True)}
    )

    def delete(self, request, pk=None):
        try:
            item = Firstbackend.objects.get(pk=pk)
        except Firstbackend.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


