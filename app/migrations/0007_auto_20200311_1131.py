# Generated by Django 3.0 on 2020-03-11 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200311_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_registration',
            name='eveningtime',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]