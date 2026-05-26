from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
import time


@api_view(['POST'])
def login(request):

    username = request.data.get('username')
    password = request.data.get('password')
    role = request.data.get('role')

    time.sleep(3)

    try:
        user = User.objects.get(
            username=username,
            password=password,
            role=role
        )

        serializer = UserSerializer(user)

        return Response({
            "status": True,
            "user": serializer.data
        })

    except:
        return Response({
            "status": False,
            "message": "Invalid Credentials"
        })


@api_view(['GET'])
def users(request):

    time.sleep(2)

    all_users = User.objects.all()

    serializer = UserSerializer(all_users, many=True)

    return Response(serializer.data)




@api_view(['DELETE'])
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return Response({"status": True})
    except:
        return Response({"status": False})
    



@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"status": True})

    return Response({"status": False})