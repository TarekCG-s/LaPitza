# Generated by Django 2.2.6 on 2019-10-27 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0011_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_item',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Order'),
        ),
    ]
