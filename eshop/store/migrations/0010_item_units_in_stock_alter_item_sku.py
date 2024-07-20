# Generated by Django 5.0.6 on 2024-07-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_item_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='units_in_stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='sku',
            field=models.CharField(default=0, max_length=50, unique=True),
        ),
    ]