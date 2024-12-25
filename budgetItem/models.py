from django.db import models
from django.utils import timezone

from fiscalYear.models import FiscalYear

# Create your models here.
class BudgetItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.CASCADE, related_name='budget_items')
    approved_amount = models.DecimalField(max_digits=15, decimal_places=2)
    planned_amount = models.DecimalField(max_digits=15, decimal_places=2)
    advanced_amount = models.DecimalField(max_digits=15, decimal_places=2)
    settled_amount = models.DecimalField(max_digits=15, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=15, decimal_places=2)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True, related_name='created_budget_items')
    updated_by = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True, related_name='updated_budget_items')

    def __str__(self):
        return self.name
