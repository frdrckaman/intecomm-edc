from bs4 import BeautifulSoup
from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from edc_constants.constants import NO, TBD, YES
from edc_dashboard.url_names import url_names
from edc_dashboard.utils import get_bootstrap_version
from edc_screening.constants import ELIGIBLE, NOT_ELIGIBLE

from intecomm_screening.models import PatientLog
from intecomm_screening.utils import (
    get_add_or_change_consent_url,
    get_add_or_change_refusal_url,
)

register = template.Library()


@register.inclusion_tag(
    f"intecomm_dashboard/bootstrap{get_bootstrap_version()}/" f"buttons/screening_button.html",
    takes_context=True,
)
def screening_button(context, model_wrapper):
    title = "Edit subject's screening form"
    perms = context["perms"]
    if model_wrapper.object.eligible is False:
        eligible = NO
    elif model_wrapper.object.eligible is True:
        eligible = YES
    else:
        eligible = TBD
    enabled = perms.user.has_perm(
        "intecomm_screening.view_subjectscreening"
    ) or perms.user.has_perm("intecomm_screening.change_subjectscreening")
    return dict(
        perms=context["perms"],
        screening_identifier=model_wrapper.object.screening_identifier,
        enabled=enabled,
        eligible=eligible,
        title=title,
        YES=YES,
        NO=NO,
        TBD=TBD,
        href=model_wrapper.href,
    )


@register.inclusion_tag(
    f"intecomm_dashboard/bootstrap{get_bootstrap_version()}/"
    f"buttons/eligibility_button.html"
)
def eligibility_button(subject_screening_model_wrapper):
    comment = []
    obj = subject_screening_model_wrapper.object
    tooltip = None
    if obj.reasons_ineligible:
        comment = obj.reasons_ineligible.split("|")
        comment = list(set(comment))
        comment.sort()
    display_label = ELIGIBLE if obj.eligible else NOT_ELIGIBLE
    soup = BeautifulSoup(display_label, features="html.parser")
    return dict(
        eligible=obj.eligible,
        eligible_final=obj.eligible,
        display_label=soup.get_text(),
        comment=comment,
        tooltip=tooltip,
        TBD=TBD,
    )


@register.inclusion_tag(
    f"intecomm_dashboard/bootstrap{get_bootstrap_version()}/buttons/add_consent_button.html",
    takes_context=True,
)
def add_consent_button(context, model_wrapper):
    title = ["Consent subject to participate."]
    consent_version = model_wrapper.consent.version

    (
        add_consent_url,
        change_consent_url,
        subject_identifier,
    ) = get_add_or_change_consent_url(
        model_wrapper.object,
        next_url_name="intecomm_dashboard:screening_listboard_url,screening_identifier",
    )
    return dict(
        perms=context["perms"],
        screening_identifier=model_wrapper.object.screening_identifier,
        href=model_wrapper.consent.href,
        consent_version=consent_version,
        title=" ".join(title),
        add_consent_url=add_consent_url,
        change_consent_url=change_consent_url,
        subject_identifier=subject_identifier,
    )


@register.inclusion_tag(
    f"intecomm_dashboard/bootstrap{get_bootstrap_version()}/"
    f"buttons/patient_log_button.html",
    takes_context=True,
)
def patient_log_button(context, model_wrapper):
    change_list_href = None
    title = "Go to patient's log"
    screening_identifier = model_wrapper.object.screening_identifier
    try:
        obj = PatientLog.objects.get(screening_identifier=screening_identifier)
    except ObjectDoesNotExist:
        pass
    else:
        change_list_href = reverse(
            "intecomm_screening_admin:intecomm_screening_patientlog_changelist"
        )
        change_list_href = f"{change_list_href}?q={obj.id}"
    return dict(
        perms=context["perms"],
        change_list_href=change_list_href,
        title=title,
    )


@register.inclusion_tag(
    f"intecomm_dashboard/bootstrap{get_bootstrap_version()}/"
    f"buttons/patient_group_button.html",
    takes_context=True,
)
def patient_group_button(context, model_wrapper):
    change_list_href = None
    patient_group = None
    title = "Go to patient's group"
    screening_identifier = model_wrapper.object.screening_identifier
    try:
        obj = PatientLog.objects.get(screening_identifier=screening_identifier)
    except ObjectDoesNotExist:
        pass
    else:
        if patient_group := obj.patientgroup_set.all().first():
            change_list_href = reverse(
                "intecomm_screening_admin:intecomm_screening_patientgroup_changelist"
            )
            change_list_href = f"{change_list_href}?q={patient_group.name}"
    return dict(
        perms=context["perms"],
        change_list_href=change_list_href,
        title=title,
        patient_group=patient_group,
    )


@register.inclusion_tag(
    f"intecomm_dashboard/bootstrap{get_bootstrap_version()}/" f"buttons/refusal_button.html",
    takes_context=True,
)
def refusal_button(context, model_wrapper):
    title = ["Capture patient's primary reason for not consenting."]
    screening_obj = model_wrapper.object
    (
        add_refusal_url,
        change_refusal_url,
    ) = get_add_or_change_refusal_url(obj=screening_obj)

    return dict(
        perms=context["perms"],
        href=change_refusal_url if change_refusal_url else add_refusal_url,
        title=" ".join(title),
    )


@register.inclusion_tag(
    f"intecomm_dashboard/bootstrap{get_bootstrap_version()}/buttons/dashboard_button.html"
)
def dashboard_button(model_wrapper):
    subject_dashboard_url = url_names.get("subject_dashboard_url")
    subject_dashboard_href = reverse(
        subject_dashboard_url, args=(model_wrapper.subject_identifier,)
    )
    title = "Go to subject's dashboard"
    return dict(
        subject_dashboard_href=subject_dashboard_href,
        subject_identifier=model_wrapper.subject_identifier,
        title=title,
    )
