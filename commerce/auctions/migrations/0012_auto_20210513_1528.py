# Generated by Django 3.1.7 on 2021-05-13 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20210512_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionlisting',
            old_name='image',
            new_name='photo',
        ),
    ]
