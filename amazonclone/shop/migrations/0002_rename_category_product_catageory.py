# Generated by Django 4.2.17 on 2025-01-09 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='catageory',
        ),
    ]
