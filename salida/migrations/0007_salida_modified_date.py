# Generated by Django 3.2.4 on 2022-06-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salida', '0006_salida_lista_personas'),
    ]

    operations = [
        migrations.AddField(
            model_name='salida',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
