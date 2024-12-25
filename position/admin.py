from django.contrib import admin
from .models import Position

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_number')
    search_fields = ('name',)
    ordering = ('order_number',)
