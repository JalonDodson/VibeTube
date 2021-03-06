# Generated by Django 3.2 on 2021-04-19 17:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('n_type', models.CharField(choices=[('M', 'MENTION'), ('L', 'LIKE'), ('C', 'COMMENT'), ('F', 'FOLLOW'), ('CR', 'COMMENT_REPLY'), ('CL', 'COMMENT_LIKE')], max_length=2)),
            ],
        ),
    ]
