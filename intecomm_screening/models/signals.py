from __future__ import annotations

from django.db.models.signals import m2m_changed, post_delete, post_save
from django.dispatch import receiver
from edc_constants.constants import COMPLETE, YES

from ..randomize_group import randomize_group
from ..utils import calculate_ratio
from . import PatientCall
from .patient_group import PatientGroup
from .patient_log import PatientLog
from .subject_screening import SubjectScreening
from .utils import add_to_group, remove_from_group


@receiver(
    post_save,
    weak=False,
    sender=PatientLog,
    dispatch_uid="update_patient_group_membership_on_patient_log_post_save",
)
def update_patient_group_on_patient_log_post_save(
    sender, instance, raw, update_fields, **kwargs
):
    if not raw and not update_fields:
        remove_from_group(instance)
        if instance.patient_group:
            add_to_group(instance)


@receiver(
    m2m_changed,
    weak=False,
    # sender=PatientGroup,
    dispatch_uid="update_patient_log_on_patient_group_m2m_change",
)
def update_patient_log_on_patient_group_m2m_change(action, instance, pk_set, **kwargs):
    if isinstance(instance, PatientGroup):
        if action == "post_remove":
            for pk in pk_set:
                patient_log = PatientLog.objects.get(id=pk)
                patient_log.patient_group = None
                patient_log.save_base(update_fields=["patient_group"])
        elif action == "post_add":
            for pk in pk_set:
                patient_log = PatientLog.objects.get(id=pk)
                patient_log.patient_group = instance
                patient_log.save_base(update_fields=["patient_group"])


@receiver(
    post_save,
    weak=False,
    sender=PatientGroup,
    dispatch_uid="update_patient_group_ratio_on_post_save",
)
def update_patient_group_ratio_on_post_save(sender, instance, raw, update_fields, **kwargs):
    if not raw and not update_fields:
        raise_on_outofrange = True if instance.status == COMPLETE else False
        ncd, hiv, ratio = calculate_ratio(
            instance.patients.all(), raise_on_outofrange=raise_on_outofrange
        )
        instance.ratio = ratio
        instance.save_base(update_fields=["ratio"])


@receiver(
    post_save,
    weak=False,
    sender=PatientGroup,
    dispatch_uid="randomize_group_on_post_save",
)
def randomize_group_on_post_save(sender, instance, raw, **kwargs):
    if not raw:
        if not instance.randomized and instance.randomize == YES:
            instance.randomized, instance.modified, instance.user_modified = randomize_group(
                instance
            )
            instance.save_base(update_fields=["randomized", "modified", "user_modified"])


@receiver(
    post_save,
    weak=False,
    sender=SubjectScreening,
    dispatch_uid="update_subjectscreening_on_post_save",
)
def update_subjectscreening_on_post_save(sender, instance, raw, **kwargs):
    if not raw:
        instance.patient_log.screening_identifier = instance.screening_identifier
        instance.patient_log.screening_datetime = instance.report_datetime
        instance.patient_log.save_base(
            update_fields=["screening_identifier", "screening_datetime"]
        )


@receiver(
    post_save,
    weak=False,
    sender=PatientCall,
    dispatch_uid="patient_call_on_post_save",
)
def patient_call_on_post_save(sender, instance, raw, created, **kwargs):
    if not raw:
        qs = sender.objects.filter(patient_log=instance.patient_log)
        instance.patient_log.call_attempts = qs.count()
        instance.patient_log.save(update_fields=["call_attempts"])


@receiver(
    post_delete,
    weak=False,
    sender=PatientCall,
    dispatch_uid="patient_call_on_post_delete",
)
def patient_call_on_post_delete(sender, instance, using, **kwargs):
    instance.patient_log.call_attempts = (
        0
        if instance.patient_log.call_attempts == 0
        else instance.patient_log.call_attempts - 1
    )
    instance.patient_log.save(update_fields=["call_attempts"])
