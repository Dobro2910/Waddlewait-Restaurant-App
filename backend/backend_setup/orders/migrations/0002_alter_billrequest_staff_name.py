# Generated by Django 5.0.3 on 2024-04-09 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billrequest',
            name='staff_name',
            field=models.CharField(default='tempStaffName', max_length=255),
        ),
    ]
