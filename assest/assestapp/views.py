from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from .models import Attandancetable,Employee
from .serializer import Empserializer,Attndanceseralizer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view 
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes

class Userview(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class Employeesview(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    serializer_class = Empserializer
    queryset = Employee.objects.all()
    permission_classes = []
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class Attandanceview(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin):
    serializer_class = Attndanceseralizer
    queryset = Attandancetable.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
   
@api_view(["GET", "PUT", "DELETE"]) 
@permission_classes([IsAuthenticated])
def user(request, id):
    if request.method == "GET":
        try:
            data = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(data)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        try:
            emp = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        try:
            data = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "DELETE"])
def attanadnce(request, id):
    try:
        data = Attandancetable.objects.get(pk=id)
    except Attandancetable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = Attndanceseralizer(data)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        data = Attandancetable.objects.get(id=id)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "PUT", "DELETE"])   
def employee(request, id):
    if request.method == "GET":
        try:
            data = Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = Empserializer(data)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        try:
            emp = Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = Empserializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        try:
            data = Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        

