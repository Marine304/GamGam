# Generated by Django 2.1.2 on 2018-10-24 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_auto_20181024_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='end_at',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='travel',
            name='start_at',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
