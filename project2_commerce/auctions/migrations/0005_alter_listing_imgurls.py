# Generated by Django 4.2.3 on 2023-11-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_rename_usercreate_listing_create_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='imgurls',
            field=models.URLField(blank=True),
        ),
    ]