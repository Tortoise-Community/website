# Generated by Django 3.2.3 on 2021-05-23 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tortoise_web', '0002_alter_events_sponsors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Changes',
            new_name='Change',
        ),
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='News',
            new_name='New',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
