# Generated by Django 3.1.7 on 2021-05-23 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_auto_20210522_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='creationdate',
            field=models.CharField(max_length=19),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentdate',
            field=models.CharField(max_length=19),
        ),
    ]