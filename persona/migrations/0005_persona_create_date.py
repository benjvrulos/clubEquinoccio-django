# Generated by Django 3.2.4 on 2022-06-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_remove_persona_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]