# Generated by Django 5.2 on 2025-04-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='Akimy', max_length=100),
        ),
    ]
