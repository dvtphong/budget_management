from django.contrib import admin
from .models import BudgetItem

@admin.register(BudgetItem)
class BudgetItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'fiscal_year', 'approved_amount', 'planned_amount', 'remaining_amount')
    list_filter = ('fiscal_year',)
    search_fields = ('name',)
