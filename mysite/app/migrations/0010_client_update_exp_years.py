# Generated by Django 5.1.3 on 2024-11-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_client_update_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_update',
            name='exp_years',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]