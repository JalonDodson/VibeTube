# Generated by Django 3.2 on 2021-04-13 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='chat_id',
            field=models.ManyToManyField(to='instant.Message', verbose_name='messages'),
        ),
    ]
