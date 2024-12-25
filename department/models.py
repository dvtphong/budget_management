from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True, related_name='created_departments')
    updated_by = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True, related_name='updated_departments')

    def __str__(self):
        return self.name