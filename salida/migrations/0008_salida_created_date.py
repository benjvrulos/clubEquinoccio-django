# Generated by Django 3.2.4 on 2022-06-23 16:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('salida', '0007_salida_modified_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='salida',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
