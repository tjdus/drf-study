from django.db import models


class RecruitmentField(models.Model):
    recruitment = models.ForeignKey(
        'Recruitment', on_delete=models.CASCADE, related_name="recruitment_field_set"
    )
    field = models.ForeignKey(
        'Field', on_delete=models.CASCADE, related_name="recruitment_field_set"
    )
    required_count = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'recruitment_fields'
        verbose_name = 'Recruitment Field'
        unique_together = ('recruitment', 'field')