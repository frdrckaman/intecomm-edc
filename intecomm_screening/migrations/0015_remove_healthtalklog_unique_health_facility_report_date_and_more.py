# Generated by Django 4.1.2 on 2022-12-01 03:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_screening", "0014_alter_historicalpatientlog_familiar_name_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="healthtalklog",
            name="unique_health_facility_report_date",
        ),
        migrations.AlterUniqueTogether(
            name="healthtalklog",
            unique_together={("health_facility", "report_date")},
        ),
    ]
