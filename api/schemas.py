# -*- coding: utf-8 -*-
from datetime import datetime

from ninja import Schema


class BookIn(Schema):
    title: str
    author: str
    publication_date: datetime


class BookOut(Schema):
    id: int
    title: str
    author: str
    publication_date: datetime
