# Generated by Django 3.0.3 on 2020-03-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tourism', '0005_places_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='offer',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
