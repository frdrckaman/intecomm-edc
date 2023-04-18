# Generated by Django 4.1.2 on 2022-11-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "intecomm_screening",
            "0002_remove_healthtalklog_unique_lower_name_report_date_and_more",
        ),
        ("intecomm_group", "0003_alter_historicalpatientgroup_group_identifier_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientgroup",
            name="patients",
            field=models.ManyToManyField(
                blank=True, to="intecomm_screening.patientlog", verbose_name="Patients"
            ),
        ),
    ]
