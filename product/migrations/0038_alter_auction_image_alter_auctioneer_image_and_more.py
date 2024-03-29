# Generated by Django 4.2 on 2024-01-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0037_rename_on_stock_auction_live'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.ImageField(upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='auctioneer',
            name='image',
            field=models.ImageField(blank=True, default='user-default.png', upload_to='auctioneer_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='image',
            field=models.ImageField(default='user-default.png', upload_to='vendor_images'),
        ),
    ]
