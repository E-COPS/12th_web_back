# Generated by Django 4.2.3 on 2023-07-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_members_std_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='comment',
            field=models.TextField(blank=True, max_length=12),
        ),
    ]