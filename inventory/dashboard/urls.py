from django.urls import path
from . import views



urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('user/', views.user, name='dashboard-user'),
    path('user/detail/<int:pk>/', views.user_detail, name='dashboard-user-detail'),
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>/', views.product_update, name='dashboard-product-update'),
    path('order/', views.order, name='dashboard-order'),
   


]
