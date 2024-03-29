# Generated by Django 4.0.3 on 2022-04-18 05:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ElectronicStore', '0022_delete_contact_remove_order_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_update',
            name='ordered_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 18, 5, 58, 25, 234277, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Name', models.CharField(max_length=100, null=True)),
                ('Cust_Address', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ElectronicStore.delivery_address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
