from django.db import models


class Recruitment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("User", on_delete=models.CASCADE, related_name="recruitment_set")


    class Meta:
        db_table = 'recruitments'
        verbose_name = 'Recruitment'
