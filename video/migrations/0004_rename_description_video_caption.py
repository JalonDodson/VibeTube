# Generated by Django 3.2 on 2021-04-06 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_video_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='description',
            new_name='caption',
        ),
    ]
