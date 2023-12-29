from django.http import JsonResponse
from .serializer import libraryserl
from .models import books
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def book_list(request , format = None):
    if request.method == 'GET':
        n = books.objects.all()
        serializer = libraryserl(n , many = True)
        return JsonResponse(serializer.data  , safe=False)
    if request.method == 'POST':
        serializer = libraryserl(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=status.HTTP_201_CREATED) 


@api_view(['GET','PUT','DELETE'])
def bookd(request , id  , format = None):
    try:
        n = books.objects.get(pk = id)
    except books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = libraryserl(n)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = libraryserl(n , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        n.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)