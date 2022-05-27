from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core import serializers
from rest_framework.generics import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import CarServices, Category
from .serializers import CategorySerializer, ServiceSerializer, UserSerializer
from rest_framework import viewsets


class UserCreateView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = CarServices.objects.all()
    serializer_class = ServiceSerializer

    def create(self, request, *args, **kwargs):
        try:
            category = get_object_or_404(Category, name=request.data.get('category'))
            owner = get_object_or_404(User, username=request.data.get('owner'))

            service = CarServices(
                category=category,
                owner=owner,
                name=request.data.get('name'),
                contact=request.data.get('contact'),
                email=request.data.get('email'),
                lat=request.data.get('lat'),
                lon=request.data.get('lon'),
                description=request.data.get('description')
            )
            service.save()
            return Response({'result': 'Service Created'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'error': 'Unable to Complete'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.CreateAPIView):
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,
                            password=password)
        if user:
            return Response({'username': username,'token': user.auth_token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User Unavailable'}, status=status.HTTP_404_NOT_FOUND)
