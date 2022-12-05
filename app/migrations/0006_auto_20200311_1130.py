# Generated by Django 3.0 on 2020-03-11 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200311_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_registration',
            name='eveningtime',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='doctor_registration',
            name='fees',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='doctor_registration',
            name='image',
            field=models.ImageField(default='', max_length=1000, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='doctor_registration',
            name='morningtime',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='doctor_registration',
            name='workingdays',
            field=models.CharField(default='', max_length=200),
        ),
    ]
