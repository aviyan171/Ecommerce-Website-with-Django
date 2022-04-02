# Generated by Django 4.0.3 on 2022-04-02 13:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ElectronicStore', '0012_remove_delivery_address_zip_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_address',
            name='Phone_Number',
            field=models.CharField(default='98032513', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='Date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 13, 18, 29, 538028, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order_update',
            name='ordered_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 2, 13, 18, 29, 539025, tzinfo=utc)),
        ),
    ]
