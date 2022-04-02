# Generated by Django 4.0.3 on 2022-04-02 12:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ElectronicStore', '0006_alter_delivery_address_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery_address',
            name='Address',
            field=models.CharField(blank=True, max_length=111, null=True),
        ),
        migrations.AlterField(
            model_name='delivery_address',
            name='Zip_code',
            field=models.CharField(blank=True, default=0, max_length=111, null=True),
        ),
        migrations.AlterField(
            model_name='delivery_address',
            name='phonenumber',
            field=models.IntegerField(blank=True, default=1, max_length=111, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='Date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 12, 36, 15, 822584, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order_update',
            name='ordered_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 2, 12, 36, 15, 822584, tzinfo=utc)),
        ),
    ]