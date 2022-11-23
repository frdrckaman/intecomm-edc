# Generated by Django 4.1.2 on 2022-11-22 20:31

import django.core.validators
from django.db import migrations
import django_crypto_fields.fields.encrypted_char_field


class Migration(migrations.Migration):

    dependencies = [
        (
            "intecomm_screening",
            "0008_rename_last_routine_appt_date_historicalpatientlog_last_appt_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="familiar_name",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Ensure name consists of letters only in upper case separated by single spaces",
                        regex="^(([A-Z]+ )*[A-Z]+)?$",
                    )
                ],
                verbose_name="How should we refer to you? (if we speak to you)",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectscreening",
            name="legal_name",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                db_index=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Ensure full name consists of letters only in upper case separated by single spaces",
                        regex="^(([A-Z]+ )*[A-Z]+)?$",
                    )
                ],
                verbose_name="Full name",
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="familiar_name",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Ensure name consists of letters only in upper case separated by single spaces",
                        regex="^(([A-Z]+ )*[A-Z]+)?$",
                    )
                ],
                verbose_name="How should we refer to you? (if we speak to you)",
            ),
        ),
        migrations.AddField(
            model_name="subjectscreening",
            name="legal_name",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Ensure full name consists of letters only in upper case separated by single spaces",
                        regex="^(([A-Z]+ )*[A-Z]+)?$",
                    )
                ],
                verbose_name="Full name",
            ),
        ),
    ]