from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'fields'
        verbose_name = 'Field'
