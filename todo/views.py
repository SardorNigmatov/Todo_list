from django.shortcuts import render
from rest_framework.views import APIView
from .models import ToDoModel
from .serializers import ToDoModelSerializers
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

# Create your views here.
class AllTask(ListAPIView):
    # def get(self,request,*args,**kwargs):
    #     all_task =ToDoModel.objects.all()
    #     serializer = ToDoModelSerializers(all_task,many=True)
    #     return Response(serializer.data,status=200)
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoModelSerializers

class DetailTask(RetrieveAPIView):
    # def get(self,request,*args,**kwargs):
    #     task = get_object_or_404(ToDoModel,id=kwargs['id'])
    #     serializer = ToDoModelSerializers(task)
    #     return Response(serializer.data,status=300)
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoModelSerializers

class CreateTask(CreateAPIView):
    # def post(self,request,*args,**kwargs):
    #     serializer = ToDoModelSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response('Task success created!!!',status=201)
    #     return Response(serializer.errors)
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoModelSerializers

class UpdateTask(UpdateAPIView):
    # def put(self,request,*args,**kwargs):
    #     task = get_object_or_404(ToDoModel,id=kwargs['id'])
    #     serializer = ToDoModelSerializers(task,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response("Task success update!!!",status=204)
    #     return Response(serializer.errors)
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoModelSerializers

class DeleteTask(DestroyAPIView):
    # def delete(self,request,*args,**kwargs):
    #     task = get_object_or_404(ToDoModel,id=kwargs['id'])
    #     task.delete()
    #     return Response("Task success deleted!",status=200)
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoModelSerializers





