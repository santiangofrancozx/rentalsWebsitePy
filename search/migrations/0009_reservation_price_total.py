# Generated by Django 4.2.5 on 2023-11-19 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_rename_client_id_reservation_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='price_total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]