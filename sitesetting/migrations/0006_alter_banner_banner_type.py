# Generated by Django 3.2.5 on 2022-02-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesetting', '0005_alter_banner_banner_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_type',
            field=models.CharField(choices=[('banner-one', 'Side-Banner'), ('banner-two', 'Main-Page-Banner'), ('banner-three', 'Game-Page-Banner'), ('banner-four', 'Blog-Page-Banner'), ('banner-five', 'Kids-Page-Banner'), ('banner-six', 'Giveaway-Page-Banner')], max_length=200, unique=True),
        ),
    ]