from django.db import models
from django.utils import timezone

from department.models import Department
from position.models import Position

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='accounts')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='accounts')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='created_accounts')
    updated_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='updated_accounts')

    def __str__(self):
        return self.fullname 