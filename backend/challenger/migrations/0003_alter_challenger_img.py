# Generated by Django 4.2.1 on 2023-07-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenger', '0002_challenger_insta_link_challenger_program_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenger',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
