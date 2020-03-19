# Generated by Django 3.0.3 on 2020-03-15 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=20)),
                ('student_dob', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
