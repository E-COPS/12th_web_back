# Generated by Django 4.2.1 on 2023-07-25 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenger', '0007_alter_challenger_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenger',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='challenger'),
        ),
    ]