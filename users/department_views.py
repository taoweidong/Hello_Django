# -*- coding: utf-8 -*-
from typing import List

from django.http import HttpRequest
from ninja import NinjaAPI
from ninja_crud import views, viewsets

from users.models import Department
from users.ninjia import router
from users.schemas import DepartmentIn, DepartmentOut

api = NinjaAPI(urls_namespace="deparment")


class DepartmentViewSet(viewsets.APIViewSet):
    api = api
    model = Department

    list_departments = views.ListView(
        response_body=List[DepartmentOut]
    )
    create_department = views.CreateView(
        request_body=DepartmentIn,
        response_body=DepartmentOut,
    )
    read_department = views.ReadView(
        response_body=DepartmentOut
    )
    update_department = views.UpdateView(
        request_body=DepartmentIn,
        response_body=DepartmentOut,
    )
    delete_department = views.DeleteView()


# 除了视图集管理的 CRUD 操作外，
# api 或路由器可以按照标准的 Django Ninja 方式使用
@router.get("/statistics/", response=dict)
def get_department_statistics(request: HttpRequest):
    return {"total": Department.objects.count()}
