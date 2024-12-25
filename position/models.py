from django.db import models
from django.utils import timezone

# Create your models here.
class Position(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    order_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True, related_name='created_positions')
    updated_by = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True, related_name='updated_positions')

    def __str__(self):
        return self.name