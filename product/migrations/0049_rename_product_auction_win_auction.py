# Generated by Django 4.2 on 2024-02-29 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0048_auction_win_delete_cartorder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction_win',
            old_name='product',
            new_name='auction',
        ),
    ]
