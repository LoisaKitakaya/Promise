# Generated by Django 4.0.5 on 2022-06-29 03:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid_amount',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='sub_total',
            field=models.CharField(default=datetime.datetime(2022, 6, 29, 3, 11, 50, 727082, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='total',
            field=models.CharField(default=datetime.datetime(2022, 6, 29, 3, 12, 5, 497765, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.CharField(max_length=200),
        ),
    ]
