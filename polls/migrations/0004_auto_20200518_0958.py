# Generated by Django 3.0.6 on 2020-05-18 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_album_musician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]