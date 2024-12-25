from django.urls import path
from . import views

app_name = 'position'

urlpatterns = [
    path('', views.position_list, name='list'),
    path('<int:pk>/', views.position_detail, name='detail'),
    path('create/', views.position_create, name='create'),
    path('<int:pk>/update/', views.position_update, name='update'),
    path('<int:pk>/delete/', views.position_delete, name='delete'),
] 