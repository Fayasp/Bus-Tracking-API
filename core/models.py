from django.db import models
from django.utils.translation import gettext_lazy as _



class AbstractModel(models.Model):
    created_by = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL,related_name="%(class)s_created", null=True, blank=True
    )
    updated_by = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL,related_name="%(class)s_updated", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
