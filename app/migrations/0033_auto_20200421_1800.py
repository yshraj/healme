# Generated by Django 3.0 on 2020-04-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20200418_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='reportdetail1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='reportdetail2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='reportdetail3',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='report',
            name='reportdetail4',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='reportdetail5',
            field=models.CharField(max_length=300),
        ),
    ]