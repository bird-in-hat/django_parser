from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt

from dj_parser.models import Page, Link 
from dj_parser.serializers import PageSerializer, LinkSerializer 

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def tags_list(request):

    if request.method == 'POST':
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'id' : serializer.data['pk'] }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def tags_detail(request, pk):

    try:
        page = Page.objects.get(pk=pk)
    except Page.DoesNotExist:
        error = {'message': 'Can not create task'}
        return Response(data=error, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PageSerializer(page, context={'request': request})
        if page.result_ready:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            error = {'message': 'Page is being parsing'}
            return Response(data=error, status=status.HTTP_417_EXPECTATION_FAILED) #??

