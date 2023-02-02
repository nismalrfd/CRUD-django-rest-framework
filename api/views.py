from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Task
from api.serializers import TaskSerializers


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail view':'/task-detail/<str:pk/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk/',
        'Delete':'/task-delete/<str:pk/',
    }
    return Response(api_urls)
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializers = TaskSerializers(tasks,many=True)
    return Response(serializers.data)
@api_view(['GET'])
def taskDetali(request,pk):
    tasks = Task.objects.get(id=pk)
    serializers = TaskSerializers(tasks,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def taskCreate(request):
    serializer =TaskSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer =TaskSerializers(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("deleted successfully")