from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TopicSerializer
from .models import Topic

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/list/',
        'Detail View':'/detail/<str:pk>/',
        'Create':'/create/',
        'Update':'/update//<str:pk>/',
        'Delete':'/delete//<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def topicList(request):
    topics = Topic.objects.all() 
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def topicDetail(request, pk):
    topics = Topic.objects.get(id=pk) 
    serializer = TopicSerializer(topics, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def topicCreate(request):
    serializer = TopicSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def topicUpdate(request, pk):
    topics = Topic.objects.get(id=pk)
    serializer = TopicSerializer(instance=topics, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def topicDelete(request, pk):
    topics = Topic.objects.get(id=pk)
    topics.delete()

    return Response("Item successfully delete!")


