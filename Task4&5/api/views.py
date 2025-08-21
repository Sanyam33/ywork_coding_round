from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def createEmp(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
                {"message": "Employee Created successfully!", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def createDep(request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
                {"message": "Departmnet Created successfully!", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getEmp(request):
    data = Employee.objects.all()
    serializer = EmployeeSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDep(request):
    data = Department.objects.all()
    serializer = DepartmentSerializer(data,many=True)
    return Response(serializer.data)