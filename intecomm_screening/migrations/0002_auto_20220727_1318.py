# Generated by Django 3.2.14 on 2022-07-27 10:18

import edc_model.validators.date
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("intecomm_screening", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="appt_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="Leave blank if continuing to the second stage today",
                null=True,
                validators=[edc_model.validators.date.date_is_past],
                verbose_name="Appointment date for second stage of screening (P2)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="appt_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="Leave blank if continuing to the second stage today",
                null=True,
                validators=[edc_model.validators.date.date_is_past],
                verbose_name="Appointment date for second stage of screening (P2)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="appt_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="Leave blank if continuing to the second stage today",
                null=True,
                validators=[edc_model.validators.date.date_is_past],
                verbose_name="Appointment date for second stage of screening (P2)",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="appt_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="Leave blank if continuing to the second stage today",
                null=True,
                validators=[edc_model.validators.date.date_is_past],
                verbose_name="Appointment date for second stage of screening (P2)",
            ),
        ),
    ]
