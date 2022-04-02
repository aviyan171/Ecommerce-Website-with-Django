# Generated by Django 4.0.3 on 2022-04-02 10:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ElectronicStore', '0003_order_update_billing_address_alter_order_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery_address',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='Date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 10, 24, 43, 932566, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order_update',
            name='ordered_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 2, 10, 24, 43, 933564, tzinfo=utc)),
        ),
    ]
