# Generated by Django 3.2.13 on 2022-07-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArvDrugs',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Arv Drugs',
                'verbose_name_plural': 'Arv Drugs',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='ArvRegimens',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'ARV Regimens',
                'verbose_name_plural': 'ARV Regimens',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='ClinicServices',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Clinic Services',
                'verbose_name_plural': 'Clinic Services',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Conditions',
                'verbose_name_plural': 'Conditions',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='DmTreatments',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Diabetes Treatments',
                'verbose_name_plural': 'Diabetes Treatments',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='DrugDispensaries',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Drug Dispensaries',
                'verbose_name_plural': 'Drug Dispensaries',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='DrugDispensers',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Drug Dispensers',
                'verbose_name_plural': 'Drug Dispensers',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='DrugPaySources',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Drug Payment Sources',
                'verbose_name_plural': 'Drug Payment Sources',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='HealthAdvisors',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Health Advisors',
                'verbose_name_plural': 'Health Advisors',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='HealthInterventionTypes',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Health Intervention Types',
                'verbose_name_plural': 'Health Intervention Types',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='HealthServices',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Health Services',
                'verbose_name_plural': 'Health Services',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='HealthTalkConditions',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Health Talk Conditions',
                'verbose_name_plural': 'Health Talk Conditions',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='HtnTreatments',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Hypertension Treatments',
                'verbose_name_plural': 'Hypertension Treatments',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='LaboratoryTests',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Laboratory Tests',
                'verbose_name_plural': 'Laboratory Tests',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='NonAdherenceReasons',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'NonAdherence Reasons',
                'verbose_name_plural': 'NonAdherence Reasons',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='OffstudyReasons',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Offstudy Reasons',
                'verbose_name_plural': 'Offstudy Reasons',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='ReasonsForTesting',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Reasons for Testing',
                'verbose_name_plural': 'Reasons for Testing',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='RefillConditions',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Refill Conditions',
                'verbose_name_plural': 'Refill Conditions',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='RxModificationReasons',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Treatment Modification Reasons',
                'verbose_name_plural': 'Treatment Modification Reasons',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='RxModifications',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Treatment Modifications',
                'verbose_name_plural': 'Treatment Modifications',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='SubjectVisitMissedReasons',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Subject Missed Visit Reasons',
                'verbose_name_plural': 'Subject Missed Visit Reasons',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='TransferReasons',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Transfer Reasons',
                'verbose_name_plural': 'Transfer Reasons',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='TransportChoices',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Transport Choices',
                'verbose_name_plural': 'Transport Choices',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='VisitReasons',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Visit Reasons',
                'verbose_name_plural': 'Visit Reasons',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.AddIndex(
            model_name='visitreasons',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_1dbf9b_idx'),
        ),
        migrations.AddIndex(
            model_name='transportchoices',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_8a0a27_idx'),
        ),
        migrations.AddIndex(
            model_name='transferreasons',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_58872e_idx'),
        ),
        migrations.AddIndex(
            model_name='subjectvisitmissedreasons',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_6fb3a6_idx'),
        ),
        migrations.AddIndex(
            model_name='rxmodifications',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_4fd810_idx'),
        ),
        migrations.AddIndex(
            model_name='rxmodificationreasons',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_c4f7bb_idx'),
        ),
        migrations.AddIndex(
            model_name='refillconditions',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_17855a_idx'),
        ),
        migrations.AddIndex(
            model_name='reasonsfortesting',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_9d7377_idx'),
        ),
        migrations.AddIndex(
            model_name='offstudyreasons',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_c1b6d2_idx'),
        ),
        migrations.AddIndex(
            model_name='nonadherencereasons',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_31cb50_idx'),
        ),
        migrations.AddIndex(
            model_name='laboratorytests',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_b0664c_idx'),
        ),
        migrations.AddIndex(
            model_name='htntreatments',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_ce0438_idx'),
        ),
        migrations.AddIndex(
            model_name='healthtalkconditions',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_21baf0_idx'),
        ),
        migrations.AddIndex(
            model_name='healthservices',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_1604f4_idx'),
        ),
        migrations.AddIndex(
            model_name='healthinterventiontypes',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_9b4020_idx'),
        ),
        migrations.AddIndex(
            model_name='healthadvisors',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_ffdb67_idx'),
        ),
        migrations.AddIndex(
            model_name='drugpaysources',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_27e420_idx'),
        ),
        migrations.AddIndex(
            model_name='drugdispensers',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_cc5dec_idx'),
        ),
        migrations.AddIndex(
            model_name='drugdispensaries',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_ffb6be_idx'),
        ),
        migrations.AddIndex(
            model_name='dmtreatments',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_aa0a3b_idx'),
        ),
        migrations.AddIndex(
            model_name='conditions',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_a3d457_idx'),
        ),
        migrations.AddIndex(
            model_name='clinicservices',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_97c7c2_idx'),
        ),
        migrations.AddIndex(
            model_name='arvregimens',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_963095_idx'),
        ),
        migrations.AddIndex(
            model_name='arvdrugs',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='intecomm_li_id_82a046_idx'),
        ),
    ]
