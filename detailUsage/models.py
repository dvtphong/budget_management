from django.db import models
from django.utils import timezone

from account.models import Account
from budgetItem.models import BudgetItem

# Create your models here.
class DetailUsage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    budget_item = models.ForeignKey(BudgetItem, on_delete=models.CASCADE, related_name='detail_usages')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='detail_usages')
    planned_amount = models.DecimalField(max_digits=15, decimal_places=2)
    advanced_amount = models.DecimalField(max_digits=15, decimal_places=2)
    settled_amount = models.DecimalField(max_digits=15, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=15, decimal_places=2)
    note = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True, related_name='created_detail_usages')
    updated_by = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True, related_name='updated_detail_usages')

    def __str__(self):
        return self.name