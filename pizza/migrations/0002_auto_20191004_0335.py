# Generated by Django 2.2.6 on 2019-10-04 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sicilian_pizza',
            old_name='items',
            new_name='toppings',
        ),
    ]
