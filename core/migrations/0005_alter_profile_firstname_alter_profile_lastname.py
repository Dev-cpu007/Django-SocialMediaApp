# Generated by Django 5.1.6 on 2025-03-28 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_profile_firstname_alter_profile_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='firstName',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastName',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
