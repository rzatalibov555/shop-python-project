from django.db import models

class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarixi")
    uptated_at = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")

    class Meta:
        abstract = True