from django.utils.translation import gettext_lazy as _
from edc_crf.model_mixins import SingletonCrfModelMixin
from edc_he.model_mixins import PropertyModelMixin
from edc_model.models import BaseUuidModel

from ...model_mixins import CrfModelMixin


class HealthEconomicsProperty(
    SingletonCrfModelMixin,
    PropertyModelMixin,
    CrfModelMixin,
    BaseUuidModel,
):
    class Meta(CrfModelMixin.Meta, BaseUuidModel.Meta):
        verbose_name = _("Health Economics: Property")
        verbose_name_plural = _("Health Economics: Property")
