# Generated by Django 4.2.2 on 2023-06-08 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]