# Generated by Django 4.2 on 2024-01-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0035_bidt_delete_bid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bidt',
            options={'verbose_name_plural': 'Bid Time'},
        ),
        migrations.AlterField(
            model_name='auctioneer',
            name='image',
            field=models.ImageField(blank=True, default='user-efault.png', upload_to='auctioneer_images'),
        ),
    ]
