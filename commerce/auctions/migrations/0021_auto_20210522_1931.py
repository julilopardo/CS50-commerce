# Generated by Django 3.1.7 on 2021-05-22 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_auto_20210520_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='buyer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]