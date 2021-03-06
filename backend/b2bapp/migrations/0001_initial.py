# Generated by Django 4.0.4 on 2022-05-01 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Write the title within 200 characters.', max_length=256)),
                ('description', models.TextField(help_text='Write a desctiprion of this blog in a few sentences')),
                ('body', models.TextField(help_text='Your main content goes here.')),
                ('views', models.IntegerField(default=0, help_text='This statistic is for your reference, do not change it.')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('privacy', models.CharField(choices=[('PRIVATE', 'Private'), ('PUBLIC', 'Public')], default='PRIVATE', help_text='Public posts will appear to everyone and private posts only to you. Change this to private instead of deleting a post.', max_length=10)),
                ('slug', models.SlugField(blank=True, help_text='Leave this parameter empty, it will get generated automatically.', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('facebookLink', models.CharField(max_length=200)),
                ('instagramLink', models.CharField(max_length=200)),
                ('twitterLink', models.CharField(max_length=200)),
                ('youtubeLink', models.CharField(max_length=200)),
                ('imageUrl', models.CharField(max_length=200)),
                ('index', models.SmallIntegerField(default=0)),
            ],
        ),
    ]
