# Generated by Django 5.1.1 on 2024-10-21 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('inventaire', '0002_objet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
        ),
    ]