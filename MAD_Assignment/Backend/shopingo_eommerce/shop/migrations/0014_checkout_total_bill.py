# Generated by Django 4.2.7 on 2024-01-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_checkout_city_alter_checkout_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='total_bill',
            field=models.FloatField(default=0),
        ),
    ]
