# Generated by Django 4.2 on 2023-12-29 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auction_duration_product_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='duration',
            field=models.PositiveIntegerField(blank=True, choices=[(3, '3 days'), (5, '5 days'), (7, '7 days')], null=True),
        ),
    ]
