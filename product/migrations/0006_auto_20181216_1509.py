# Generated by Django 2.1.4 on 2018-12-16 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20181214_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='central_eating',
            new_name='central_heating',
        ),
    ]
