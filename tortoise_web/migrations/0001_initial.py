# Generated by Django 3.0.7 on 2020-12-20 09:22

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import utils.misc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Changes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('prize', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=100)),
                ('task', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('cover_image', models.ImageField(upload_to='img/bgimgs')),
                ('event_image', models.ImageField(blank=True, upload_to='img/eventimgs')),
                ('status', models.CharField(choices=[('Live', 'Live'), ('Ended', 'Ended'), ('Upcoming', 'Upcoming')], default='Ended', max_length=17)),
                ('event_type', models.CharField(choices=[('Other Event', 'Other'), ('CTF Event', 'CTF-Event'), ('Team Challenge', 'Team-Challenge'), ('Coding Challenge', 'Coding-Challenge')], default='CTF Event', max_length=17)),
                ('style', models.CharField(choices=[('default.min.css', 'Default'), ('dark.min.css', 'Dark'), ('dracula.min.css', 'Dracula'), ('tomorrow.min.css', 'Tomorrow'), ('night-owl.min.css', 'Night Owl'), ('codepen-embed.min.css', 'Codepen'), ('github-gist.min.css', 'Github Gist'), ('atom-one-dark.min.css', 'Atom Dark'), ('solarized-dark.min.css', 'Solarized Dark'), ('atelier-cave-dark.min.css', 'Atelier Cave'), ('tomorrow-night-blue.css', 'Tomorrow Night Blue'), ('atom-one-dark-reasonable.min.css', 'Atom Dark Reasonable')], default='default.min.css', max_length=50)),
                ('page_theme', models.CharField(choices=[('event-light-theme', 'Light Theme'), ('event-dark-theme', 'Dark Theme'), ('event-ares-theme', 'Ares Theme'), ('event-nemesis-theme', 'Nemesis Theme'), ('event-grass-hopper-theme', 'Grasshopper Theme')], default='event-light-theme', max_length=35)),
                ('due_date', models.DateField()),
                ('end_date', models.DateField()),
                ('sponsors', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=utils.misc.empty_dict)),
                ('winner', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.TextField()),
                ('choice', models.CharField(choices=[('News', 'News'), ('Live', 'Live'), ('Announcements', 'Announcements')], default='Live', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=150)),
                ('content', models.TextField(blank=True)),
                ('extra', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('cover_image', models.ImageField(upload_to='img/bgimgs')),
                ('rating', models.FloatField(blank=True, default=0.0)),
                ('label', models.CharField(max_length=100)),
                ('brief', models.TextField()),
                ('status', models.CharField(choices=[('cata red', 'Started'), ('cata green', 'Upcoming'), ('cata yellow', 'Completed'), ('cata purple', 'Refactoring')], default='cata purple', max_length=16)),
                ('github', models.URLField(blank=True)),
                ('invite', models.URLField(blank=True)),
                ('commits', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('stars', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('forks', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('contributors', models.PositiveSmallIntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_crumb_1', models.CharField(blank=True, default='', max_length=20)),
                ('head_crumb_2', models.CharField(blank=True, default='', max_length=20)),
                ('span', models.CharField(blank=True, default='', max_length=20)),
                ('slide_image_url', models.URLField(blank=True)),
                ('sub_head', models.CharField(blank=True, default='', max_length=50)),
                ('note', models.TextField(blank=True, default='')),
                ('button', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('nickname', models.CharField(max_length=15)),
                ('profile_img', models.ImageField(upload_to='img/team')),
                ('designation', models.CharField(help_text='Complete this, what is it?', max_length=12)),
            ],
        ),
    ]
