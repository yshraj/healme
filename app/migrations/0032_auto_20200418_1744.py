# Generated by Django 3.0 on 2020-04-18 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20200418_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportbooking',
            name='reports',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.Report'),
        ),
    ]
