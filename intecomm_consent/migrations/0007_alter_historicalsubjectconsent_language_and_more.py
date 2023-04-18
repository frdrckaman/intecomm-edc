# Generated by Django 4.1.2 on 2023-02-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_consent", "0006_historicalsubjectconsent_group_identifier_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalsubjectconsent",
            name="language",
            field=models.CharField(
                choices=[
                    ["sw", "Swahili"],
                    ["en", "English"],
                    ["mas", "Maasai"],
                    ["ry", "Runyakitara"],
                    ["lg", "Luganda"],
                    ["rny", "Runyankore"],
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
                    ["sw", "Swahili"],
                    ["en", "English"],
                    ["mas", "Maasai"],
                    ["ry", "Runyakitara"],
                    ["lg", "Luganda"],
                    ["rny", "Runyankore"],
                ],
                help_text="The language used for the consent process will also be used during data collection.",
                max_length=25,
                verbose_name="Language of consent",
            ),
        ),
    ]
