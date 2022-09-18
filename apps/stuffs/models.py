from django.db import models
from django.utils.translation import gettext_lazy as _
from django_measurement.models import MeasurementField
from measurement.measures import Weight, Distance
from simple_history.models import HistoricalRecords
from apps.stuffs.uuid import BaseUUID

# Create your models here.


class Staff(BaseUUID):
    # agent = models.ForeignKey(Agent, related_name='agent_stuffs', on_delete=models.CASCADE)
    item = models.CharField(_("Item"), max_length=50, blank=True, null=True)
    # item_count = models.IntegerField(_("Count of item"))
    item_weight = MeasurementField(measurement=Weight, default=0)
    item_serial_number = models.CharField(
        _("Serial number"), max_length=20, blank=True, null=True)
    item_part_number = models.CharField(
        _("Part number"), max_length=20, blank=True, null=True)
    item_lenght = MeasurementField(measurement=Distance, blank=True, null=True)
    item_width = MeasurementField(measurement=Distance, blank=True, null=True)
    item_height = MeasurementField(measurement=Distance, blank=True, null=True)
    image_document = models.FileField(blank=True, null=True)


    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.item}"


class Aog(Staff):
    image = models.ImageField(
        upload_to='images/stuffs/aog', null=True, blank=True)

    def __str__(self):
        return self.item

    def image_tag(self):
        return u'<img src="%s" width="300"/>' % self.image.url  # Not bad code
    image_tag.allow_tags = True
    item_serial_number = None
    item_part_number = models.CharField(
        _("Part number"), max_length=20, blank=True, null=True)
    item_history = HistoricalRecords()

    def __str__(self, *args):
        return f"{self.item} - {self.item_weight} | {self.item_part_number}"


class AcStand(Staff):
    image = models.ImageField(
        upload_to='images/stuffs/stands', null=True, blank=True)

    def __str__(self):
        return self.item

    def image_tag(self):
        return u'<img src="%s" width="300"/>' % self.image.url  # Not bad code
    image_tag.allow_tags = True


class Instrument(Staff):

    image = models.ImageField(
        upload_to='images/stuffs/instr', null=True, blank=True)

    def __str__(self):
        return self.item

    def image_tag(self):
        return u'<img src="%s" width="300"/>' % self.image.url  # Not bad code
    image_tag.allow_tags = True


class AcEngine(Staff):

    image = models.ImageField(
        upload_to='images/stuffs/engins', null=True, blank=True)

    def __str__(self):
        return f"{self.item} - {self.item_weight}"

    def image_tag(self):
        return u'<img src="%s" width="300"/>' % self.image.url  # Not bad code
    image_tag.allow_tags = True
