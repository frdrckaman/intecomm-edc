# Generated by Django 3.2.13 on 2022-07-03 14:44

import _socket
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_crypto_fields.fields.encrypted_char_field
import django_revision.revision_field
import edc_model_fields.fields.other_charfield
import edc_screening.model_mixins.screening_fields_model_mixin
import edc_sites.models
import edc_utils.date
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectScreening',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50)),
                ('subject_identifier_as_pk', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('subject_identifier_aka', models.CharField(editable=False, help_text='track a previously allocated identifier.', max_length=50, null=True, verbose_name='Subject Identifier a.k.a')),
                ('slug', models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True)),
                ('eligible', models.BooleanField(default=False, editable=False)),
                ('reasons_ineligible', models.TextField(editable=False, max_length=150, null=True, verbose_name='Reason not eligible')),
                ('eligibility_datetime', models.DateTimeField(editable=False, help_text='Date and time eligibility was determined relative to report_datetime', null=True)),
                ('real_eligibility_datetime', models.DateTimeField(editable=False, help_text='Date and time eligibility was determined relative to now', null=True)),
                ('reference', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Reference')),
                ('screening_identifier', models.CharField(blank=True, editable=False, max_length=50, unique=True, verbose_name='Screening ID')),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, help_text='Date and time of report.', verbose_name='Report Date and Time')),
                ('initials', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text='Use UPPERCASE letters only. May be 2 or 3 letters. (Encryption: RSA local)', max_length=71, validators=[django.core.validators.RegexValidator('[A-Z]{1,3}', 'Invalid format'), django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(3)])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('age_in_years', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(110)])),
                ('consent_ability', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Participant or legal guardian/representative able and willing to give informed consent.')),
                ('unsuitable_for_study', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', help_text='If YES, patient NOT eligible, please give reason below.', max_length=5, verbose_name='Is there any other reason the patient is deemed to not be suitable for the study?')),
                ('reasons_unsuitable', models.TextField(blank=True, max_length=150, null=True, verbose_name='Reason not suitable for the study')),
                ('unsuitable_agreed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='Does the study coordinator agree that the patient is not suitable for the study?')),
                ('consented', models.BooleanField(default=False, editable=False)),
                ('refused', models.BooleanField(default=False, editable=False)),
                ('screening_consent', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, verbose_name='Has the subject given his/her verbal consent to be screened for the INTECOMM trial?')),
                ('hospital_identifier', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, unique=True)),
                ('lives_nearby', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, verbose_name='Is the patient living within the catchment population of the facility')),
                ('staying_nearby_12', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, null=True, verbose_name='Is the patient planning to remain in the catchment area for at least 12 months')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'Subject Screening',
                'verbose_name_plural': 'Subject Screening',
            },
            managers=[
                ('on_site', edc_sites.models.CurrentSiteManager()),
                ('objects', edc_screening.model_mixins.screening_fields_model_mixin.ScreeningManager()),
            ],
        ),
        migrations.CreateModel(
            name='SubjectRefusal',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier_as_pk', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('subject_identifier_aka', models.CharField(editable=False, help_text='track a previously allocated identifier.', max_length=50, null=True, verbose_name='Subject Identifier a.k.a')),
                ('subject_identifier', models.CharField(editable=False, max_length=50)),
                ('screening_identifier', models.CharField(editable=False, max_length=50)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, verbose_name='Report Date and Time')),
                ('reason', models.CharField(max_length=25, verbose_name='Reason for refusal to join')),
                ('other_reason', edc_model_fields.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.site')),
                ('subject_screening', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='intecomm_screening.subjectscreening')),
            ],
            options={
                'verbose_name': 'Subject Refusal',
                'verbose_name_plural': 'Subject Refusals',
            },
            managers=[
                ('on_site', edc_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalSubjectScreening',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('subject_identifier', models.CharField(max_length=50)),
                ('subject_identifier_as_pk', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('subject_identifier_aka', models.CharField(editable=False, help_text='track a previously allocated identifier.', max_length=50, null=True, verbose_name='Subject Identifier a.k.a')),
                ('slug', models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True)),
                ('eligible', models.BooleanField(default=False, editable=False)),
                ('reasons_ineligible', models.TextField(editable=False, max_length=150, null=True, verbose_name='Reason not eligible')),
                ('eligibility_datetime', models.DateTimeField(editable=False, help_text='Date and time eligibility was determined relative to report_datetime', null=True)),
                ('real_eligibility_datetime', models.DateTimeField(editable=False, help_text='Date and time eligibility was determined relative to now', null=True)),
                ('reference', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='Reference')),
                ('screening_identifier', models.CharField(blank=True, db_index=True, editable=False, max_length=50, verbose_name='Screening ID')),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, help_text='Date and time of report.', verbose_name='Report Date and Time')),
                ('initials', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text='Use UPPERCASE letters only. May be 2 or 3 letters. (Encryption: RSA local)', max_length=71, validators=[django.core.validators.RegexValidator('[A-Z]{1,3}', 'Invalid format'), django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(3)])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('age_in_years', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(110)])),
                ('consent_ability', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Participant or legal guardian/representative able and willing to give informed consent.')),
                ('unsuitable_for_study', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', help_text='If YES, patient NOT eligible, please give reason below.', max_length=5, verbose_name='Is there any other reason the patient is deemed to not be suitable for the study?')),
                ('reasons_unsuitable', models.TextField(blank=True, max_length=150, null=True, verbose_name='Reason not suitable for the study')),
                ('unsuitable_agreed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='Does the study coordinator agree that the patient is not suitable for the study?')),
                ('consented', models.BooleanField(default=False, editable=False)),
                ('refused', models.BooleanField(default=False, editable=False)),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('screening_consent', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, verbose_name='Has the subject given his/her verbal consent to be screened for the INTECOMM trial?')),
                ('hospital_identifier', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, db_index=True, help_text=' (Encryption: RSA local)', max_length=71)),
                ('lives_nearby', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, verbose_name='Is the patient living within the catchment population of the facility')),
                ('staying_nearby_12', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15, null=True, verbose_name='Is the patient planning to remain in the catchment area for at least 12 months')),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Subject Screening',
                'verbose_name_plural': 'historical Subject Screening',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSubjectRefusal',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('subject_identifier_as_pk', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('subject_identifier_aka', models.CharField(editable=False, help_text='track a previously allocated identifier.', max_length=50, null=True, verbose_name='Subject Identifier a.k.a')),
                ('subject_identifier', models.CharField(editable=False, max_length=50)),
                ('screening_identifier', models.CharField(editable=False, max_length=50)),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, verbose_name='Report Date and Time')),
                ('reason', models.CharField(max_length=25, verbose_name='Reason for refusal to join')),
                ('other_reason', edc_model_fields.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...')),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
                ('subject_screening', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='intecomm_screening.subjectscreening')),
            ],
            options={
                'verbose_name': 'historical Subject Refusal',
                'verbose_name_plural': 'historical Subject Refusals',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
