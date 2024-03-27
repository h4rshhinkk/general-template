import os
import uuid

from core.base import BaseModel
from django.db import models
from django.urls import reverse_lazy


class Department(BaseModel):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    

    def get_absolute_url(self):
        return reverse_lazy("employees:department_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("employees:department_list")

    def get_update_url(self):
        return reverse_lazy("employees:department_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("employees:department_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)




