# Generated by Django 3.1.7 on 2021-05-20 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auto_20210520_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='currentbid',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]