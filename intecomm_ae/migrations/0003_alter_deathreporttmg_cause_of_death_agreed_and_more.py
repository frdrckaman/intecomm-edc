# Generated by Django 4.1.2 on 2023-01-23 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("intecomm_ae", "0002_rename_narrative_aetmg_investigator_narrative_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deathreporttmg",
            name="cause_of_death_agreed",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="If No, explain in the narrative below",
                max_length=15,
                null=True,
                verbose_name="Is the cause of death agreed between study doctor and TMG member?",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldeathreporttmg",
            name="cause_of_death_agreed",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="If No, explain in the narrative below",
                max_length=15,
                null=True,
                verbose_name="Is the cause of death agreed between study doctor and TMG member?",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldeathreporttmgsecond",
            name="cause_of_death_agreed",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="If No, explain in the narrative below",
                max_length=15,
                null=True,
                verbose_name="Is the cause of death agreed between study doctor and TMG member?",
            ),
        ),
    ]
