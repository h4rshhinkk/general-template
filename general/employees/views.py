from django.db.models import F
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone

from . import tables
from .models import Department
from core import mixins


class DepartmentListView(mixins.HybridListView):
    model = Department
    table_class = tables.DepartmentTable
    filterset_fields = ("name",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Departments"
        context["can_add"] = True
        context["new_link"] = reverse_lazy("employees:department_create")
        return context


class DepartmentDetailView(mixins.HybridDetailView):
    model = Department


class DepartmentCreateView(mixins.HybridCreateView):
    model = Department
    exclude = ("creator", "is_active")


class DepartmentUpdateView(mixins.HybridUpdateView):
    model = Department
    exclude = ("creator", "is_active")


class DepartmentDeleteView(mixins.HybridDeleteView):
    model = Department

