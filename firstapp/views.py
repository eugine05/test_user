from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from firstapp.models import User

from firstapp.serializers import (UserSerializer,)


class UserRoot(APIView):
    """Пользователи"""
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        userlast = request.GET.get("userlast")
        if userlast=='load':
            users = User.objects.all()[:10]
        else:
            users = User.objects.filter(id__gt=userlast)[:5]
        serializer = UserSerializer(users, many=True)
        return Response({"data": serializer.data})

    def patch(self, request):
        user_id = request.data.get("id")
        user = User.objects.get(id=user_id)
        print(user_id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)
    
    def delete(self, request):
        user_id = request.data.get("id")
        user = User.objects.get(id=user_id)
        user.delete()
        return Response(status=201)

    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(serializer.errors,status=400)


# sfsdlfks;dlfksl;d
# qweqw
