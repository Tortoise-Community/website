# Generated by Django 3.0.7 on 2020-09-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20200926_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='roles',
            field=models.ManyToManyField(blank=True, null=True, to='userdata.Role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
