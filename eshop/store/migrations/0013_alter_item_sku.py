# Generated by Django 5.0.6 on 2024-07-04 14:05

import store.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_item_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sku',
            field=models.CharField(default=store.models.generate_sku, max_length=50, unique=True),
        ),
    ]
