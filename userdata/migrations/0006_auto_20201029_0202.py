# Generated by Django 3.0.7 on 2020-10-28 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0005_auto_20201029_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='tag',
            field=models.CharField(default=0, max_length=6),
        ),
    ]
