# Generated by Django 5.0.6 on 2024-07-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_userprofile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cart',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]