# Generated by Django 4.1.2 on 2022-10-19 22:55

from django.db import migrations, models
import django.db.models.deletion
import edc_model.validators.date


class Migration(migrations.Migration):

    dependencies = [
        ("intecomm_subject", "0001_initial"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="cd4result",
            name="intecomm_su_subject_35596d_idx",
        ),
        migrations.RemoveIndex(
            model_name="cd4result",
            name="intecomm_su_subject_85e709_idx",
        ),
        migrations.RenameField(
            model_name="cd4result",
            old_name="result",
            new_name="cd4_value",
        ),
        migrations.RenameField(
            model_name="historicalcd4result",
            old_name="result",
            new_name="cd4_value",
        ),
        migrations.RemoveField(
            model_name="cd4result",
            name="crf_status",
        ),
        migrations.RemoveField(
            model_name="cd4result",
            name="crf_status_comments",
        ),
        migrations.RemoveField(
            model_name="cd4result",
            name="drawn_date",
        ),
        migrations.RemoveField(
            model_name="historicalcd4result",
            name="crf_status",
        ),
        migrations.RemoveField(
            model_name="historicalcd4result",
            name="crf_status_comments",
        ),
        migrations.RemoveField(
            model_name="historicalcd4result",
            name="drawn_date",
        ),
        migrations.RemoveField(
            model_name="historicalhivreview",
            name="test_date",
        ),
        migrations.RemoveField(
            model_name="historicalviralloadresult",
            name="drawn_date",
        ),
        migrations.RemoveField(
            model_name="hivreview",
            name="test_date",
        ),
        migrations.RemoveField(
            model_name="viralloadresult",
            name="drawn_date",
        ),
        migrations.AddField(
            model_name="cd4result",
            name="assay_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="Result assay date and time",
            ),
        ),
        migrations.AddField(
            model_name="cd4result",
            name="cd4_units",
            field=models.CharField(
                default="cells/mm^3", editable=False, max_length=25, verbose_name="Units"
            ),
        ),
        migrations.AddField(
            model_name="cd4result",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                help_text="Start typing the requisition identifier or select one from this visit",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="intecomm_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AddField(
            model_name="dmreview",
            name="care_delivery",
            field=models.CharField(
                choices=[
                    ("health_facility", "Health facility"),
                    ("community_clinic", "Community clinic"),
                    ("OTHER", "Other facility, please specify below ..."),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="Care for this `condition` was delivered today at ...",
            ),
        ),
        migrations.AddField(
            model_name="dmreview",
            name="care_delivery_other",
            field=models.TextField(
                blank=True, null=True, verbose_name="If other facility, please specify"
            ),
        ),
        migrations.AddField(
            model_name="historicalcd4result",
            name="assay_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="Result assay date and time",
            ),
        ),
        migrations.AddField(
            model_name="historicalcd4result",
            name="cd4_units",
            field=models.CharField(
                default="cells/mm^3", editable=False, max_length=25, verbose_name="Units"
            ),
        ),
        migrations.AddField(
            model_name="historicalcd4result",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="Start typing the requisition identifier or select one from this visit",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="intecomm_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AddField(
            model_name="historicaldmreview",
            name="care_delivery",
            field=models.CharField(
                choices=[
                    ("health_facility", "Health facility"),
                    ("community_clinic", "Community clinic"),
                    ("OTHER", "Other facility, please specify below ..."),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="Care for this `condition` was delivered today at ...",
            ),
        ),
        migrations.AddField(
            model_name="historicaldmreview",
            name="care_delivery_other",
            field=models.TextField(
                blank=True, null=True, verbose_name="If other facility, please specify"
            ),
        ),
        migrations.AddField(
            model_name="historicalviralloadresult",
            name="assay_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="Result assay date and time",
            ),
        ),
        migrations.AddField(
            model_name="historicalviralloadresult",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "viral_load"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="intecomm_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AddField(
            model_name="historicalviralloadresult",
            name="vl_units",
            field=models.CharField(
                default="copies/mL", editable=False, max_length=25, verbose_name="Units"
            ),
        ),
        migrations.AddField(
            model_name="viralloadresult",
            name="assay_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="Result assay date and time",
            ),
        ),
        migrations.AddField(
            model_name="viralloadresult",
            name="requisition",
            field=models.ForeignKey(
                blank=True,
                help_text="Start typing the requisition identifier or select one from this visit",
                limit_choices_to={"panel__name": "viral_load"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="intecomm_subject.subjectrequisition",
                verbose_name="Requisition",
            ),
        ),
        migrations.AddField(
            model_name="viralloadresult",
            name="vl_units",
            field=models.CharField(
                default="copies/mL", editable=False, max_length=25, verbose_name="Units"
            ),
        ),
        migrations.AlterField(
            model_name="historicalhivreview",
            name="care_delivery",
            field=models.CharField(
                choices=[
                    ("health_facility", "Health facility"),
                    ("community_clinic", "Community clinic"),
                    ("OTHER", "Other facility, please specify below ..."),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="Care for this `condition` was delivered today at ...",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhivreview",
            name="care_delivery_other",
            field=models.TextField(
                blank=True, null=True, verbose_name="If other facility, please specify"
            ),
        ),
        migrations.AlterField(
            model_name="historicalhtnreview",
            name="care_delivery",
            field=models.CharField(
                choices=[
                    ("health_facility", "Health facility"),
                    ("community_clinic", "Community clinic"),
                    ("OTHER", "Other facility, please specify below ..."),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="Care for this `condition` was delivered today at ...",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhtnreview",
            name="care_delivery_other",
            field=models.TextField(
                blank=True, null=True, verbose_name="If other facility, please specify"
            ),
        ),
        migrations.AlterField(
            model_name="historicalviralloadresult",
            name="vl_quantifier",
            field=models.CharField(
                choices=[("=", "="), (">", ">"), ("<", "<")],
                default="=",
                max_length=10,
                verbose_name="Quantifier",
            ),
        ),
        migrations.AlterField(
            model_name="hivreview",
            name="care_delivery",
            field=models.CharField(
                choices=[
                    ("health_facility", "Health facility"),
                    ("community_clinic", "Community clinic"),
                    ("OTHER", "Other facility, please specify below ..."),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="Care for this `condition` was delivered today at ...",
            ),
        ),
        migrations.AlterField(
            model_name="hivreview",
            name="care_delivery_other",
            field=models.TextField(
                blank=True, null=True, verbose_name="If other facility, please specify"
            ),
        ),
        migrations.AlterField(
            model_name="htnreview",
            name="care_delivery",
            field=models.CharField(
                choices=[
                    ("health_facility", "Health facility"),
                    ("community_clinic", "Community clinic"),
                    ("OTHER", "Other facility, please specify below ..."),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=25,
                verbose_name="Care for this `condition` was delivered today at ...",
            ),
        ),
        migrations.AlterField(
            model_name="htnreview",
            name="care_delivery_other",
            field=models.TextField(
                blank=True, null=True, verbose_name="If other facility, please specify"
            ),
        ),
        migrations.AlterField(
            model_name="viralloadresult",
            name="vl_quantifier",
            field=models.CharField(
                choices=[("=", "="), (">", ">"), ("<", "<")],
                default="=",
                max_length=10,
                verbose_name="Quantifier",
            ),
        ),
    ]
