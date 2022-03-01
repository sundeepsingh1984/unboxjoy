# Generated by Django 3.2.5 on 2022-02-18 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedType',
            fields=[
                ('feed_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('feed_type_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('feed_id', models.AutoField(primary_key=True, serialize=False)),
                ('feed_code', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('feed_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialfeeds.feedtype')),
            ],
        ),
    ]
