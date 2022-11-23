from edc_constants.constants import (
    CLINICAL_ENDPOINT,
    DEAD,
    DM,
    HIV,
    HTN,
    NCD,
    NOT_APPLICABLE,
    OTHER,
    PREGNANCY,
    TOXICITY,
)
from edc_ltfu.constants import LOST_TO_FOLLOWUP
from edc_offstudy.constants import COMPLETED_FOLLOWUP, CONSENT_WITHDRAWAL
from edc_transfer.constants import TRANSFERRED

from intecomm_prn.constants import (
    CLINICAL_WITHDRAWAL,
    LATE_EXCLUSION,
    OTHER_RX_DISCONTINUATION,
)
from intecomm_subject.constants import INTEGRATED

list_data = {
    "intecomm_lists.offstudyreasons": [
        (COMPLETED_FOLLOWUP, "Patient completed 36 months of follow-up"),
        (CLINICAL_WITHDRAWAL, "Patient is withdrawn on CLINICAL grounds ..."),
        (CLINICAL_ENDPOINT, "Patient reached a clinical endpoint"),
        (TOXICITY, "Patient experienced an unacceptable toxicity"),
        (
            "intercurrent_illness",
            "Intercurrent illness which prevents further treatment",
        ),
        (LOST_TO_FOLLOWUP, "Patient lost to follow-up"),
        (DEAD, "Patient reported/known to have died"),
        (CONSENT_WITHDRAWAL, "Patient withdrew consent to participate further"),
        (LATE_EXCLUSION, "Patient fulfilled late exclusion criteria*"),
        (TRANSFERRED, "Patient has been transferred to another health centre"),
        (
            OTHER_RX_DISCONTINUATION,
            "Other condition that justifies the discontinuation of "
            "treatment in the clinician’s opinion (specify below)",
        ),
        (
            OTHER,
            "Other reason (specify below)",
        ),
    ],
    "intecomm_lists.subjectvisitmissedreasons": [
        ("forgot", "Forgot / Can’t remember being told about appointment"),
        ("family_emergency", "Family emergency (e.g. funeral) and was away"),
        ("travelling", "Away travelling/visiting"),
        ("working_schooling", "Away working/schooling"),
        ("too_sick", "Too sick or weak to come to the centre"),
        ("lack_of_transport", "Transportation difficulty"),
        (OTHER, "Other reason (specify below)"),
    ],
    "intecomm_lists.clinicalwithdrawalreasons": [
        (PREGNANCY, "Pregnancy"),
        ("kidney_disease", "Development of chronic kidney disease"),
        ("liver_disease", "Development of chronic liver disease"),
        ("intercurrent_illness", "Intercurrent illness which prevents further treatment"),
        ("investigator_decision", "Investigator decision"),
        (NOT_APPLICABLE, "Not applicable"),
        (
            OTHER,
            (
                "Other condition that justifies the discontinuation of "
                "treatment in the clinician’s opinion (specify below)"
            ),
        ),
    ],
    "intecomm_lists.toxicitywithdrawalreasons": [
        ("lactic_acidosis", "Development of lactic acidosis or hyperlactatemia"),
        ("hepatomegaly", "Development of hepatomegaly with steatosis"),
        (NOT_APPLICABLE, "Not applicable"),
        (OTHER, "Other (specify below)"),
    ],
    "intecomm_lists.healthtalktypes": [
        ("study_intro_talk", "INTECOMM study introduction"),
        ("sensitisation_talk", "INTECOMM Sensitisation"),
        (OTHER, "Other (specify below)"),
    ],
    "intecomm_lists.conditions": [
        (HIV, "HIV"),
        (DM, "Diabetes"),
        (HTN, "Hypertension"),
    ],
    "intecomm_lists.healthfacilitytypes": [
        (DM, "Diabetes Clinic"),
        (HIV, "HIV Clinic"),
        (HTN, "Hypertension Clinic"),
        (INTEGRATED, "Integrated Clinic (HIV/NCD)"),
        (NCD, "NCD Clinic"),
        (OTHER, "Other (specify below)"),
    ],
    "intecomm_lists.locationtypes": [
        ("school", "School"),
        (OTHER, "Other (specify below)"),
    ],
}