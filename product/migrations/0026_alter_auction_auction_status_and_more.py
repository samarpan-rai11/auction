# Generated by Django 4.2 on 2024-01-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_alter_auction_auction_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_status',
            field=models.CharField(choices=[('process', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('process', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='processing', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('process', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='in_review', max_length=10),
        ),
    ]
