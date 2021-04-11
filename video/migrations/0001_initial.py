# Generated by Django 3.2 on 2021-04-09 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import vibetube.helpers
import video.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=60, null=True)),
                ('likes', models.IntegerField(default=0)),
                ('replies', models.JSONField(default=video.models.default_replies)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(upload_to='')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sound_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.IntegerField(default=vibetube.helpers.gen_uuid, unique=True)),
                ('video', models.FileField(upload_to=vibetube.helpers.user_vid_path)),
                ('privacy', models.CharField(choices=[('F', 'Friends'), ('PRV', 'Private'), ('PUB', 'Public')], max_length=3)),
                ('likes', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('caption', models.CharField(max_length=70)),
                ('comments', models.ManyToManyField(blank=True, to='video.Comment')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_creator', to=settings.AUTH_USER_MODEL)),
                ('sound', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vid_sound', to='video.sound')),
            ],
        ),
        migrations.AddField(
            model_name='sound',
            name='original_video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='og_sound', to='video.video'),
        ),
    ]
