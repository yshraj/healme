# Generated by Django 3.0 on 2020-03-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_diagnostic_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_registration',
            name='eveningtime',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor_registration',
            name='fees',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor_registration',
            name='image',
            field=models.ImageField(max_length=1000, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='doctor_registration',
            name='morningtime',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor_registration',
            name='workingdays',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
