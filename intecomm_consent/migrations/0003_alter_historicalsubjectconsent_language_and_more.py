# Generated by Django 4.1.2 on 2022-11-30 01:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "intecomm_consent",
            "0002_remove_subjectconsent_intecomm_co_subject_145905_idx_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalsubjectconsent",
            name="language",
            field=models.CharField(
                choices=[
                    ["lg", "Luganda"],
                    ["ry", "Runyakitara"],
                    ["en", "English"],
                    ["sw", "Swahili"],
                    ["mas", "Maasai"],
                ],
                help_text="The language used for the consent process will also be used during data collection.",
                max_length=25,
                verbose_name="Language of consent",
            ),
        ),
        migrations.AlterField(
            model_name="subjectconsent",
            name="language",
            field=models.CharField(
                choices=[
                    ["lg", "Luganda"],
                    ["ry", "Runyakitara"],
                    ["en", "English"],
                    ["sw", "Swahili"],
                    ["mas", "Maasai"],
                ],
                help_text="The language used for the consent process will also be used during data collection.",
                max_length=25,
                verbose_name="Language of consent",
            ),
        ),
    ]
