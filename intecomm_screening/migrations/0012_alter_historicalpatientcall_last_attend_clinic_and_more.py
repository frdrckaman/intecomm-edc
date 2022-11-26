# Generated by Django 4.1.2 on 2022-11-25 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "intecomm_screening",
            "0011_rename_hf_identifier_historicalpatientlog_hospital_identifier_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalpatientcall",
            name="last_attend_clinic",
            field=models.CharField(
                blank=True,
                help_text="This may be helpful when updating health records",
                max_length=25,
                null=True,
                verbose_name="Where did the patient last seek care",
            ),
        ),
        migrations.AlterField(
            model_name="patientcall",
            name="last_attend_clinic",
            field=models.CharField(
                blank=True,
                help_text="This may be helpful when updating health records",
                max_length=25,
                null=True,
                verbose_name="Where did the patient last seek care",
            ),
        ),
    ]
