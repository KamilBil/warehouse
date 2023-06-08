from django.db import models
from simple_history.models import HistoricalRecords

class Group(models.Model):
    external_id = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=256, default="")
    history = HistoricalRecords()
    unique_together = (("external_id"),)

    def __str__(self):
        return "{} {}".format(self.pk, self.name)

class Post(models.Model):
    external_id = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    added_in_social_media = models.DateTimeField(null=True, blank=True)
    text_value = models.TextField(default="", null=True, blank=True)
    label = models.TextField(default="", null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    history = HistoricalRecords()

    class Meta:
        unique_together = (("external_id"),)

    def __str__(self):
        short_val = self.text_value[0:50]
        if len(short_val) < len(str(self.text_value)):
            short_val += "..."
        return "ext_id:{} {}".format(self.pk, short_val)