# Generated by Django 3.2 on 2021-04-15 10:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0003_comment_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='like_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
