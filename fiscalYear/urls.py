from django.urls import path
from . import views

app_name = 'fiscal_year'

urlpatterns = [
    path('', views.fiscal_year_list, name='list'),
    path('<int:pk>/', views.fiscal_year_detail, name='detail'),
    path('create/', views.fiscal_year_create, name='create'),
    path('<int:pk>/update/', views.fiscal_year_update, name='update'),
    path('<int:pk>/delete/', views.fiscal_year_delete, name='delete'),
] 