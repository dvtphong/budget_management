from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'position', 'department', 'email', 'phone_number')
    list_filter = ('position', 'department')
    search_fields = ('fullname', 'email', 'phone_number')
