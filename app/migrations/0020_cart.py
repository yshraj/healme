# Generated by Django 3.0 on 2020-03-16 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_pharma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Patient_registration')),
                ('pharma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pharma')),
            ],
        ),
    ]
