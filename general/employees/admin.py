from core.base import BaseAdmin
from django.contrib import admin

from .models import Department


@admin.register(Department)
class DepartmentAdmin(BaseAdmin):
    list_display = ("name", "description", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    ordering = ("name",)




 
