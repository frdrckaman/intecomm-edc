from edc_visit_schedule import Crf, FormsCollection

# TODO: whats the difference between bloodresultsglu and glucose??

crfs_prn = FormsCollection(
    Crf(show_order=10, model="intecomm_subject.bloodresultsfbc"),
    Crf(show_order=150, model="intecomm_subject.glucose"),
    Crf(show_order=220, model="intecomm_subject.bloodresultsglu"),
    Crf(show_order=230, model="intecomm_subject.bloodresultshba1c"),
    Crf(show_order=240, model="intecomm_subject.bloodresultsrft"),
    Crf(show_order=250, model="intecomm_subject.bloodresultslft"),
    Crf(show_order=260, model="intecomm_subject.bloodresultslipid"),
    Crf(show_order=270, model="intecomm_subject.hepatitistest"),
    Crf(show_order=280, model="intecomm_subject.malariatest"),
    Crf(show_order=290, model="intecomm_subject.urinedipsticktest"),
    Crf(show_order=360, model="intecomm_subject.concomitantmedication"),
    Crf(show_order=380, model="intecomm_subject.urinepregnancy"),
    Crf(show_order=1000, model="intecomm_subject.pregnancyupdate"),
    name="prn",
)

crfs_d1 = FormsCollection(
    Crf(show_order=100, model="intecomm_subject.clinicalreviewbaseline"),
    Crf(show_order=110, model="intecomm_subject.indicators"),
    Crf(show_order=120, model="intecomm_subject.hivinitialreview", required=False),
    Crf(show_order=130, model="intecomm_subject.dminitialreview", required=False),
    Crf(show_order=140, model="intecomm_subject.htninitialreview", required=False),
    Crf(show_order=143, model="intecomm_subject.medications"),
    Crf(show_order=145, model="intecomm_subject.drugrefillhtn", required=False),
    Crf(show_order=150, model="intecomm_subject.drugrefilldm", required=False),
    Crf(show_order=155, model="intecomm_subject.drugrefillhiv", required=False),
    Crf(show_order=160, model="intecomm_subject.otherbaselinedata"),
    Crf(show_order=165, model="intecomm_subject.complicationsbaseline"),
    name="day1",
)

crfs_1m = FormsCollection(
    Crf(show_order=110, model="intecomm_subject.clinicalreview"),
    Crf(show_order=115, model="intecomm_subject.indicators"),
    Crf(show_order=112, model="intecomm_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="intecomm_subject.dminitialreview", required=False),
    Crf(show_order=116, model="intecomm_subject.htninitialreview", required=False),
    Crf(show_order=130, model="intecomm_subject.hivreview", required=False),
    Crf(show_order=140, model="intecomm_subject.dmreview", required=False),
    Crf(show_order=150, model="intecomm_subject.htnreview", required=False),
    Crf(show_order=155, model="intecomm_subject.medications"),
    Crf(show_order=160, model="intecomm_subject.drugrefillhtn", required=False),
    Crf(show_order=170, model="intecomm_subject.drugrefilldm", required=False),
    Crf(show_order=180, model="intecomm_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="intecomm_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="intecomm_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="intecomm_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="intecomm_subject.complicationsfollowup", required=False),
    Crf(show_order=220, model="intecomm_subject.familyhistory"),
    name="2m",
)
crfs_2m = FormsCollection(
    Crf(show_order=110, model="intecomm_subject.clinicalreview"),
    Crf(show_order=115, model="intecomm_subject.indicators"),
    Crf(show_order=112, model="intecomm_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="intecomm_subject.dminitialreview", required=False),
    Crf(show_order=116, model="intecomm_subject.htninitialreview", required=False),
    Crf(show_order=130, model="intecomm_subject.hivreview", required=False),
    Crf(show_order=140, model="intecomm_subject.dmreview", required=False),
    Crf(show_order=150, model="intecomm_subject.htnreview", required=False),
    Crf(show_order=155, model="intecomm_subject.medications"),
    Crf(show_order=160, model="intecomm_subject.drugrefillhtn", required=False),
    Crf(show_order=170, model="intecomm_subject.drugrefilldm", required=False),
    Crf(show_order=180, model="intecomm_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="intecomm_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="intecomm_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="intecomm_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="intecomm_subject.complicationsfollowup", required=False),
    name="2m",
)
crfs_3m = FormsCollection(
    Crf(show_order=110, model="intecomm_subject.clinicalreview"),
    Crf(show_order=115, model="intecomm_subject.indicators"),
    Crf(show_order=112, model="intecomm_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="intecomm_subject.dminitialreview", required=False),
    Crf(show_order=116, model="intecomm_subject.htninitialreview", required=False),
    Crf(show_order=130, model="intecomm_subject.hivreview", required=False),
    Crf(show_order=140, model="intecomm_subject.dmreview", required=False),
    Crf(show_order=150, model="intecomm_subject.htnreview", required=False),
    Crf(show_order=155, model="intecomm_subject.medications"),
    Crf(show_order=160, model="intecomm_subject.drugrefillhtn", required=False),
    Crf(show_order=170, model="intecomm_subject.drugrefilldm", required=False),
    Crf(show_order=180, model="intecomm_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="intecomm_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="intecomm_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="intecomm_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="intecomm_subject.complicationsfollowup", required=False),
    name="3m",
)
crfs_4m = FormsCollection(
    Crf(show_order=110, model="intecomm_subject.clinicalreview"),
    Crf(show_order=115, model="intecomm_subject.indicators"),
    Crf(show_order=112, model="intecomm_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="intecomm_subject.dminitialreview", required=False),
    Crf(show_order=116, model="intecomm_subject.htninitialreview", required=False),
    Crf(show_order=130, model="intecomm_subject.hivreview", required=False),
    Crf(show_order=140, model="intecomm_subject.dmreview", required=False),
    Crf(show_order=150, model="intecomm_subject.htnreview", required=False),
    Crf(show_order=155, model="intecomm_subject.medications"),
    Crf(show_order=160, model="intecomm_subject.drugrefillhtn", required=False),
    Crf(show_order=170, model="intecomm_subject.drugrefilldm", required=False),
    Crf(show_order=180, model="intecomm_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="intecomm_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="intecomm_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="intecomm_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="intecomm_subject.complicationsfollowup", required=False),
    name="4m",
)
crfs_5m = FormsCollection(
    Crf(show_order=110, model="intecomm_subject.clinicalreview"),
    Crf(show_order=115, model="intecomm_subject.indicators"),
    Crf(show_order=112, model="intecomm_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="intecomm_subject.dminitialreview", required=False),
    Crf(show_order=116, model="intecomm_subject.htninitialreview", required=False),
    Crf(show_order=130, model="intecomm_subject.hivreview", required=False),
    Crf(show_order=140, model="intecomm_subject.dmreview", required=False),
    Crf(show_order=150, model="intecomm_subject.htnreview", required=False),
    Crf(show_order=155, model="intecomm_subject.medications"),
    Crf(show_order=160, model="intecomm_subject.drugrefillhtn", required=False),
    Crf(show_order=170, model="intecomm_subject.drugrefilldm", required=False),
    Crf(show_order=180, model="intecomm_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="intecomm_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="intecomm_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="intecomm_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="intecomm_subject.complicationsfollowup", required=False),
    name="5m",
)
crfs_6m = FormsCollection(
    Crf(show_order=110, model="intecomm_subject.clinicalreview"),
    Crf(show_order=115, model="intecomm_subject.indicators"),
    Crf(show_order=112, model="intecomm_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="intecomm_subject.dminitialreview", required=False),
    Crf(show_order=116, model="intecomm_subject.htninitialreview", required=False),
    Crf(show_order=130, model="intecomm_subject.hivreview", required=False),
    Crf(show_order=140, model="intecomm_subject.dmreview", required=False),
    Crf(show_order=150, model="intecomm_subject.htnreview", required=False),
    Crf(show_order=155, model="intecomm_subject.medications"),
    Crf(show_order=160, model="intecomm_subject.drugrefillhtn", required=False),
    Crf(show_order=170, model="intecomm_subject.drugrefilldm", required=False),
    Crf(show_order=180, model="intecomm_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="intecomm_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="intecomm_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="intecomm_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="intecomm_subject.complicationsfollowup", required=False),
    name="6m",
)
crfs_7m = FormsCollection(
    Crf(show_order=110, model="intecomm_subject.clinicalreview"),
    Crf(show_order=115, model="intecomm_subject.indicators"),
    Crf(show_order=112, model="intecomm_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="intecomm_subject.dminitialreview", required=False),
    Crf(show_order=116, model="intecomm_subject.htninitialreview", required=False),
    Crf(show_order=130, model="intecomm_subject.hivreview", required=False),
    Crf(show_order=140, model="intecomm_subject.dmreview", required=False),
    Crf(show_order=150, model="intecomm_subject.htnreview", required=False),
    Crf(show_order=155, model="intecomm_subject.medications"),
    Crf(show_order=160, model="intecomm_subject.drugrefillhtn", required=False),
    Crf(show_order=170, model="intecomm_subject.drugrefilldm", required=False),
    Crf(show_order=180, model="intecomm_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="intecomm_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="intecomm_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="intecomm_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="intecomm_subject.complicationsfollowup", required=False),
    name="7m",
)
crfs_8m = FormsCollection(
    Crf(show_order=110, model="intecomm_subject.clinicalreview"),
    Crf(show_order=115, model="intecomm_subject.indicators"),
    Crf(show_order=112, model="intecomm_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="intecomm_subject.dminitialreview", required=False),
    Crf(show_order=116, model="intecomm_subject.htninitialreview", required=False),
    Crf(show_order=130, model="intecomm_subject.hivreview", required=False),
    Crf(show_order=140, model="intecomm_subject.dmreview", required=False),
    Crf(show_order=150, model="intecomm_subject.htnreview", required=False),
    Crf(show_order=155, model="intecomm_subject.medications"),
    Crf(show_order=160, model="intecomm_subject.drugrefillhtn", required=False),
    Crf(show_order=170, model="intecomm_subject.drugrefilldm", required=False),
    Crf(show_order=180, model="intecomm_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="intecomm_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="intecomm_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="intecomm_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="intecomm_subject.complicationsfollowup", required=False),
    name="8m",
)
crfs_9m = FormsCollection(
    Crf(show_order=110, model="intecomm_subject.clinicalreview"),
    Crf(show_order=115, model="intecomm_subject.indicators"),
    Crf(show_order=112, model="intecomm_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="intecomm_subject.dminitialreview", required=False),
    Crf(show_order=116, model="intecomm_subject.htninitialreview", required=False),
    Crf(show_order=130, model="intecomm_subject.hivreview", required=False),
    Crf(show_order=140, model="intecomm_subject.dmreview", required=False),
    Crf(show_order=150, model="intecomm_subject.htnreview", required=False),
    Crf(show_order=155, model="intecomm_subject.medications"),
    Crf(show_order=160, model="intecomm_subject.drugrefillhtn", required=False),
    Crf(show_order=170, model="intecomm_subject.drugrefilldm", required=False),
    Crf(show_order=180, model="intecomm_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="intecomm_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="intecomm_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="intecomm_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="intecomm_subject.complicationsfollowup", required=False),
    name="9m",
)
crfs_10m = FormsCollection(
    Crf(show_order=110, model="intecomm_subject.clinicalreview"),
    Crf(show_order=115, model="intecomm_subject.indicators"),
    Crf(show_order=112, model="intecomm_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="intecomm_subject.dminitialreview", required=False),
    Crf(show_order=116, model="intecomm_subject.htninitialreview", required=False),
    Crf(show_order=130, model="intecomm_subject.hivreview", required=False),
    Crf(show_order=140, model="intecomm_subject.dmreview", required=False),
    Crf(show_order=150, model="intecomm_subject.htnreview", required=False),
    Crf(show_order=155, model="intecomm_subject.medications"),
    Crf(show_order=160, model="intecomm_subject.drugrefillhtn", required=False),
    Crf(show_order=170, model="intecomm_subject.drugrefilldm", required=False),
    Crf(show_order=180, model="intecomm_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="intecomm_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="intecomm_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="intecomm_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="intecomm_subject.complicationsfollowup", required=False),
    name="10m",
)
crfs_11m = FormsCollection(
    Crf(show_order=110, model="intecomm_subject.clinicalreview"),
    Crf(show_order=115, model="intecomm_subject.indicators"),
    Crf(show_order=112, model="intecomm_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="intecomm_subject.dminitialreview", required=False),
    Crf(show_order=116, model="intecomm_subject.htninitialreview", required=False),
    Crf(show_order=130, model="intecomm_subject.hivreview", required=False),
    Crf(show_order=140, model="intecomm_subject.dmreview", required=False),
    Crf(show_order=150, model="intecomm_subject.htnreview", required=False),
    Crf(show_order=155, model="intecomm_subject.medications"),
    Crf(show_order=160, model="intecomm_subject.drugrefillhtn", required=False),
    Crf(show_order=170, model="intecomm_subject.drugrefilldm", required=False),
    Crf(show_order=180, model="intecomm_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="intecomm_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="intecomm_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="intecomm_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="intecomm_subject.complicationsfollowup", required=False),
    name="11m",
)
crfs_12m = FormsCollection(
    Crf(show_order=110, model="intecomm_subject.clinicalreview"),
    Crf(show_order=115, model="intecomm_subject.indicators"),
    Crf(show_order=112, model="intecomm_subject.hivinitialreview", required=False),
    Crf(show_order=114, model="intecomm_subject.dminitialreview", required=False),
    Crf(show_order=116, model="intecomm_subject.htninitialreview", required=False),
    Crf(show_order=120, model="intecomm_subject.hivreview", required=False),
    Crf(show_order=130, model="intecomm_subject.dmreview", required=False),
    Crf(show_order=140, model="intecomm_subject.htnreview", required=False),
    Crf(show_order=145, model="intecomm_subject.medications"),
    Crf(show_order=150, model="intecomm_subject.drugrefillhtn", required=False),
    Crf(show_order=160, model="intecomm_subject.drugrefilldm", required=False),
    Crf(show_order=170, model="intecomm_subject.drugrefillhiv", required=False),
    Crf(show_order=185, model="intecomm_subject.hivmedicationadherence", required=False),
    Crf(show_order=190, model="intecomm_subject.dmmedicationadherence", required=False),
    Crf(show_order=195, model="intecomm_subject.htnmedicationadherence", required=False),
    Crf(show_order=200, model="intecomm_subject.complicationsfollowup", required=False),
    name="12m",
)

crfs_unscheduled = FormsCollection(
    # Crf(show_order=10, model="intecomm_subject.followupvitals"),
    name="unscheduled",
)

crfs_missed = FormsCollection(
    Crf(show_order=10, model="intecomm_subject.subjectvisitmissed"),
    name="missed",
)