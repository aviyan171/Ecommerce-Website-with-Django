# Generated by Django 4.0.3 on 2022-04-03 08:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ElectronicStore', '0015_order_update_customer_name_alter_order_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='Date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 3, 8, 38, 55, 817226, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order_update',
            name='ordered_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 3, 8, 38, 55, 818224, tzinfo=utc)),
        ),
    ]