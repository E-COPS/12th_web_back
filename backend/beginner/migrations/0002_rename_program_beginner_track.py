# Generated by Django 4.2.1 on 2023-07-25 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beginner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beginner',
            old_name='program',
            new_name='track',
        ),
    ]
