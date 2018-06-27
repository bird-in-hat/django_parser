from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from dj_parser.models import Page, Link 
from dj_parser.serializers import PageSerializer, LinkSerializer 

# Create your views here.

@csrf_exempt #???
@api_view(['POST'])
def tags_list(request):
    """
    Create a new page.
    """
    if request.method == 'POST':
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Celery send task
            # set code PENDING
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def tags_detail(request, pk):
    """
    Retrieve a page instance.
    """
    try:
        product = Page.objects.get(pk=pk)
    except Page.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PageSerializer(product,context={'request': request})
        return Response(serializer.data)
