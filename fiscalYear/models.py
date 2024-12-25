from django.db import models
from django.utils import timezone


class FiscalYear(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    note = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True, related_name='created_fiscal_years')
    updated_by = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True, related_name='updated_fiscal_years')

    def __str__(self):
        return self.name