from core.base import BaseTable

from .models import Department



class DepartmentTable(BaseTable):
    class Meta:
        model = Department
        fields = ("name", "is_active")
        attrs = {"class": "table key-buttons border-bottom"}


