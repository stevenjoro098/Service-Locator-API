from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.authtoken.models import Token
from .models import Category, CarServices
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['image','name', 'slug']


class ServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = CarServices
        fields = ['pk', 'category', 'name', 'contact', 'email', 'description', 'lat', 'lon']

    def create(self, validated_data):
        print('Validated data is : ', validated_data)
        category = get_object_or_404(Category, name="Programming")
        owner = get_object_or_404(User, username='cars')
        service = CarServices(
            category=category,
            owner=owner,
            name=validated_data['name'],
            contact=validated_data['contact'],
            email=validated_data['email'],
            lat=validated_data['lat'],
            lon=validated_data['lon'],
            description=validated_data['description']
        )
        service.save()
        return service
