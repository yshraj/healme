# Generated by Django 3.0 on 2020-03-16 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_medicines_pharmacy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', max_length=1000, upload_to='images')),
                ('name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
        ),
    ]
