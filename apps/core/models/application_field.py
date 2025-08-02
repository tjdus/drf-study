from django.db import models


class ApplicationField(models.Model):
    application = models.ForeignKey(
        'Application', on_delete=models.CASCADE, related_name="application_field_set"
    )
    field = models.ForeignKey(
        'Field', on_delete=models.CASCADE, related_name="application_field_set"
    )

    class Meta:
        db_table = 'application_fields'
        verbose_name = 'Application Field'
        unique_together = ('application', 'field')