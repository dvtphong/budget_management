from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.account_list, name='list'),
    path('<int:pk>/', views.account_detail, name='detail'),
    path('create/', views.account_create, name='create'),
    path('<int:pk>/update/', views.account_update, name='update'),
    path('<int:pk>/delete/', views.account_delete, name='delete'),
] 