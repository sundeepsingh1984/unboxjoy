# Generated by Django 3.2.5 on 2022-03-03 08:40

import django.core.validators
from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sitesetting', '0012_feeds_socialmediafeedtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_address', django_quill.fields.QuillField()),
                ('phoneNumber', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Information',
        ),
    ]