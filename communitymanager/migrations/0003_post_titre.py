# Generated by Django 2.2 on 2021-05-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0002_post_priorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='titre',
            field=models.CharField(default='title', max_length=50),
        ),
    ]
