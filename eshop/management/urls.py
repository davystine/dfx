from django.urls import path
from . import views
from .views import (
    UserListView, UserCreateView, UserUpdateView, UserDeleteView,)

app_name = 'management'  # Namespace for this app

urlpatterns = [
    # Item URLs
    path('items/', views.ItemListView.as_view(), name='item_list'),
    path('items/add/', views.ItemCreateView.as_view(), name='item_add'),
    path('items/edit/<int:pk>/', views.ItemUpdateView.as_view(), name='item_edit'),
    path('items/delete/<int:pk>/', views.ItemDeleteView.as_view(), name='item_delete'),
    
    # Category URLs
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('categories/edit/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # User URLs
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),

]
