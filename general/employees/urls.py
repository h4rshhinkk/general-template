from django.urls import path

from . import views


app_name = "employees"

urlpatterns = [
    
    path("department/", views.DepartmentListView.as_view(), name="department_list"),
    path("department/<str:pk>/", views.DepartmentDetailView.as_view(), name="department_detail"),
    path("new/department/", views.DepartmentCreateView.as_view(), name="department_create"),
    path("department/<str:pk>/update/", views.DepartmentUpdateView.as_view(), name="department_update"),
    path("department/<str:pk>/delete/", views.DepartmentDeleteView.as_view(), name="department_delete"),
   
]
