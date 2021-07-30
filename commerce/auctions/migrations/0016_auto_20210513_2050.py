# Generated by Django 3.1.7 on 2021-05-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20210513_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('listingid', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentdate',
            field=models.CharField(max_length=200),
        ),
    ]
