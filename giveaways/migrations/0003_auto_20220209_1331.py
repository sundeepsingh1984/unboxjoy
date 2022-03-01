# Generated by Django 3.2.5 on 2022-02-09 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giveaways', '0002_auto_20220209_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giveawayregistration',
            name='player',
        ),
        migrations.AddField(
            model_name='giveawayregistration',
            name='player',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='giveaways.player'),
            preserve_default=False,
        ),
    ]