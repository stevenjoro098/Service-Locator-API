from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('services', views.ServicesViewSet, basename='services')

urlpatterns = [
    path('api/category/', views.CategoryView.as_view(), name='category_list'),
    path('api/user/', views.UserCreateView.as_view(), name='create_user'),
    path('api/user/login/', views.LoginView.as_view(), name='login')
]

urlpatterns += router.urls
