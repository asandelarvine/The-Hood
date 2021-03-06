# Generated by Django 3.2.9 on 2022-01-07 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0007_rename_owner_business_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=600, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.location')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighborhood')),
            ],
        ),
    ]
