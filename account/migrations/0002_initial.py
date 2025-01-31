# Generated by Django 5.1.4 on 2024-12-25 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('department', '0001_initial'),
        ('position', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='department.department'),
        ),
        migrations.AddField(
            model_name='account',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='position.position'),
        ),
        migrations.AddField(
            model_name='account',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_accounts', to='account.account'),
        ),
    ]
