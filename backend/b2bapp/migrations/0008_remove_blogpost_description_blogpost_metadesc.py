# Generated by Django 4.0.4 on 2022-05-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b2bapp', '0007_alter_blogpost_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='description',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='metadesc',
            field=models.CharField(default='', help_text='Write a desctiprion of this blog in a few sentences', max_length=512),
            preserve_default=False,
        ),
    ]