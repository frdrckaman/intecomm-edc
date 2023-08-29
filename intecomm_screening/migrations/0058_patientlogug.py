# Generated by Django 4.2.4 on 2023-08-26 22:51

from django.db import migrations
import edc_sites.model_mixins
import intecomm_screening.models.patient_log


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_screening", "0057_alter_consentrefusal_device_created_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PatientLogUg",
            fields=[],
            options={
                "verbose_name": "Patient Log (Uganda)",
                "verbose_name_plural": "Patient Log (Uganda)",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("intecomm_screening.patientlog",),
            managers=[
                ("objects", intecomm_screening.models.patient_log.PatientLogManager()),
                ("on_site", edc_sites.model_mixins.CurrentSiteManager()),
            ],
        ),
    ]
