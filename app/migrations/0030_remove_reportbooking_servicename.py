# Generated by Django 3.0 on 2020-04-18 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_report_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportbooking',
            name='servicename',
        ),
    ]
