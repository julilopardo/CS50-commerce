# Generated by Django 3.1.7 on 2021-05-12 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210511_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='buyer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='auctions.user'),
        ),
    ]
