# Generated by Django 4.2.3 on 2023-07-26 18:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_facility", "0002_auto_20230726_2030"),
        ("intecomm_screening", "0053_rename_idenfifierformat_identifierformat_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="healthtalklog",
            unique_together={("health_facility", "report_date")},
        ),
    ]
