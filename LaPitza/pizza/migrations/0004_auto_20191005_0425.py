# Generated by Django 2.2.6 on 2019-10-05 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_dinner_platter_pasta_salad_sub_topping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('small', models.FloatField(default=0)),
                ('large', models.FloatField(default=0)),
                ('toppings', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name='Dinner_platter',
        ),
        migrations.DeleteModel(
            name='Pasta',
        ),
        migrations.DeleteModel(
            name='Regular_pizza',
        ),
        migrations.DeleteModel(
            name='Salad',
        ),
        migrations.DeleteModel(
            name='Sicilian_pizza',
        ),
        migrations.DeleteModel(
            name='Sub',
        ),
        migrations.AddField(
            model_name='topping',
            name='large',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='topping',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='topping',
            name='small',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Type'),
        ),
    ]
