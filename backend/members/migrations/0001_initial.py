# Generated by Django 4.2.1 on 2023-07-23 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('img', models.ImageField(upload_to='photos/')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True)),
                ('insta_link', models.URLField(blank=True)),
                ('git_link', models.URLField(blank=True)),
                ('linkedin_link', models.URLField(blank=True)),
                ('tf', models.BooleanField(default=False)),
            ],
        ),
    ]
