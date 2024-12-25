from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
    path('departments/', include('department.urls')),
    path('positions/', include('position.urls')),
    path('fiscal-years/', include('fiscalYear.urls')),
]
