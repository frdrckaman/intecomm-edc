# Generated by Django 4.2.1 on 2023-07-01 20:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_screening", "0038_auto_20230701_0117"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicalpatientlog",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Patient Log",
                "verbose_name_plural": "historical Patient Log",
            },
        ),
        migrations.AlterModelOptions(
            name="patientlog",
            options={
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Patient Log",
                "verbose_name_plural": "Patient Log",
            },
        ),
    ]
