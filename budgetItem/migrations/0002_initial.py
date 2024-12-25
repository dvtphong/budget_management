# Generated by Django 5.1.4 on 2024-12-25 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_initial'),
        ('budgetItem', '0001_initial'),
        ('fiscalYear', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetitem',
            name='fiscal_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budget_items', to='fiscalYear.fiscalyear'),
        ),
        migrations.AddField(
            model_name='budgetitem',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_budget_items', to='account.account'),
        ),
    ]