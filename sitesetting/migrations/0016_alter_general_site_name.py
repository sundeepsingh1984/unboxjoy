# Generated by Django 3.2.5 on 2022-03-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesetting', '0015_contactrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general',
            name='site_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
