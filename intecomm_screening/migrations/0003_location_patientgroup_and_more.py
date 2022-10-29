# Generated by Django 4.1.2 on 2022-10-28 18:32

import _socket
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_crypto_fields.fields.encrypted_char_field
import django_crypto_fields.fields.encrypted_text_field
import django_revision.revision_field
import edc_sites.models
import edc_utils.date
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("intecomm_lists", "0002_healthtalks_healthtalks_intecomm_li_id_a3e2b7_idx"),
        ("sites", "0002_alter_domain_unique"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("intecomm_screening", "0002_alter_historicalsubjectscreening_art_adherent_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        unique=True,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "plural_name",
                    models.CharField(max_length=250, null=True, verbose_name="Plural name"),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                ("version", models.CharField(default="1.0", editable=False, max_length=35)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "verbose_name": "Location",
                "verbose_name_plural": "Locations",
            },
        ),
        migrations.CreateModel(
            name="PatientGroup",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=25, unique=True, verbose_name="Group name"
                    ),
                ),
            ],
            managers=[
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="htn_complications",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=15,
                verbose_name="Does the patient suffer from any complications of hypertension that are unmanaged or uncontrolled.",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="selection_method",
            field=models.CharField(
                choices=[
                    ("random_sampling", "Random sampling"),
                    ("purposively_selected", "Purposively selected"),
                ],
                default="purposively_selected",
                max_length=25,
                verbose_name="How was the patient selected for screening?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.site",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="htn_complications",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=15,
                verbose_name="Does the patient suffer from any complications of hypertension that are unmanaged or uncontrolled.",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="selection_method",
            field=models.CharField(
                choices=[
                    ("random_sampling", "Random sampling"),
                    ("purposively_selected", "Purposively selected"),
                ],
                default="purposively_selected",
                max_length=25,
                verbose_name="How was the patient selected for screening?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="site",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="sites.site",
            ),
        ),
        migrations.CreateModel(
            name="PatientLog",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "screening_identifier",
                    models.CharField(
                        editable=False,
                        help_text="Auto populated when screening form is complete",
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "screening_datetime",
                    models.DateTimeField(
                        editable=False,
                        help_text="Auto populated when screening form is complete",
                        null=True,
                    ),
                ),
                (
                    "name",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True, help_text=" (Encryption: RSA local)", max_length=71
                    ),
                ),
                ("report_datetime", models.DateTimeField(default=edc_utils.date.get_utcnow)),
                (
                    "hf_identifier",
                    models.CharField(
                        max_length=25, unique=True, verbose_name="Health facility identifier"
                    ),
                ),
                (
                    "contact_number",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                    ),
                ),
                (
                    "alt_contact_number",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                    ),
                ),
                (
                    "location_description",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=71,
                        null=True,
                    ),
                ),
                (
                    "stable",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("tbd", "To be determined")],
                        default="tbd",
                        max_length=15,
                        verbose_name="Do the facility health care staff consider the patient stable in care",
                    ),
                ),
                (
                    "last_routine_appt_date",
                    models.DateField(
                        blank=True,
                        help_text="May help to estimate next appt",
                        null=True,
                        verbose_name="When was the patient last seen at this health facility",
                    ),
                ),
                (
                    "next_routine_appt_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="When is the patient next scheduled for a routine appointment at this health facility",
                    ),
                ),
                (
                    "first_health_talk",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                        default="unknown",
                        max_length=15,
                        verbose_name="Attended general INTECOMM health talk",
                    ),
                ),
                ("first_health_talk_date", models.DateField(blank=True, null=True)),
                (
                    "second_health_talk",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                        default="unknown",
                        max_length=15,
                        verbose_name="Attended INTECOMM sensitisation session",
                    ),
                ),
                (
                    "second_health_talk_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Sensitisation session date"
                    ),
                ),
                (
                    "conditions",
                    models.ManyToManyField(
                        to="intecomm_lists.conditions",
                        verbose_name="Conditions with a documented diagnosis",
                    ),
                ),
                (
                    "patient_group",
                    models.ForeignKey(
                        help_text="Auto populated when screening form is complete",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="intecomm_screening.patientgroup",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="sites.site",
                        verbose_name="Health facility",
                    ),
                ),
            ],
            options={
                "verbose_name": "Patient Log",
                "verbose_name_plural": "Patient Log",
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
            },
            managers=[
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name="patientgroup",
            name="patients",
            field=models.ManyToManyField(
                limit_choices_to={"consented": False, "eligible": True},
                to="intecomm_screening.subjectscreening",
            ),
        ),
        migrations.AddField(
            model_name="patientgroup",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="sites.site",
            ),
        ),
        migrations.CreateModel(
            name="HistoricalPatientGroup",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                (
                    "name",
                    models.CharField(db_index=True, max_length=25, verbose_name="Group name"),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sites.site",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical patient group",
                "verbose_name_plural": "historical patient groups",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
