# Generated by Django 5.0.1 on 2024-01-31 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0011_alter_payments_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]