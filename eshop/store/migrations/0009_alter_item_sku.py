# Generated by Django 5.0.6 on 2024-07-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_item_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sku',
            field=models.CharField(default='4CE404', max_length=50, unique=True),
        ),
    ]