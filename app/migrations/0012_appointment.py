# Generated by Django 3.0 on 2020-03-11 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200311_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Patient_registration')),
            ],
        ),
    ]