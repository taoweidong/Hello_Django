# -*- coding: utf-8 -*-
from typing import List

from django.http import HttpRequest
from ninja_crud import views, viewsets

from api.api import ninja_api
from api.models import Book
from api.schemas import BookOut, BookIn

book_api = ninja_api


class BookViewSet(viewsets.APIViewSet):
    api = book_api
    model = Book

    list_Books = views.ListView(
        response_body=List[BookOut]
    )
    create_Book = views.CreateView(
        request_body=BookIn,
        response_body=BookOut,
    )
    read_Book = views.ReadView(
        response_body=BookOut
    )
    update_Book = views.UpdateView(
        request_body=BookIn,
        response_body=BookOut,
    )
    delete_Book = views.DeleteView()


# 除了视图集管理的 CRUD 操作外，
# api 或路由器可以按照标准的 Django Ninja 方式使用
@book_api.get("/statistics/", response=dict)
def get_Book_statistics(request: HttpRequest):
    return {"total": Book.objects.count()}
