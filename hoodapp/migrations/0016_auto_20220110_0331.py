# Generated by Django 3.2.9 on 2022-01-10 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0015_alter_health_logo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk']},
        ),
    ]
