# Generated by Django 3.2 on 2021-04-19 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibe_user', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viber',
            name='bio',
            field=models.TextField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='viber',
            name='display_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
