# Generated by Django 4.2 on 2024-01-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0040_alter_auction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.ImageField(default='default-product-image.png', upload_to='auction_images'),
        ),
    ]