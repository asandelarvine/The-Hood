# Generated by Django 3.2.9 on 2022-01-07 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0005_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='hoodapp.neighborhood'),
        ),
    ]