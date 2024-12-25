from django.contrib import admin
from .models import DetailUsage

@admin.register(DetailUsage)
class DetailUsageAdmin(admin.ModelAdmin):
    list_display = ('name', 'budget_item', 'account', 'planned_amount', 'remaining_amount', 'due_date')
    list_filter = ('budget_item', 'account', 'due_date')
    search_fields = ('name',)
