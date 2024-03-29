# Generated by Django 4.2 on 2024-01-01 06:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0014_cartorder_order_auction_auction_status_auction_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='image',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='invoice_no',
            field=models.CharField(default='001', max_length=100),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='item',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='orders',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.order'),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('process', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='processing', max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='order',
            name='paid_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_time', models.DateTimeField(auto_now_add=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.order')),
            ],
        ),
    ]
