from typing import Optional

from ninja import Schema

from Hello_Django.ninja import ninja_api


class Item(Schema):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int


@ninja_api.get("/list")
def list_posts(request):
    return {"posts": ["Post 1", "Post 2"]}


# Create your views here.
@ninja_api.get("/posts", description="查询数据的接口的描述詳情", summary="查询数据的接口")
def list_posts(request):
    """
    查询接口
    :param request:入参\r\n
    :return: 返回详情数据
    """
    return {"posts": ["Post 1", "Post 2"]}


@ninja_api.post("/items")
def create(request, item: Item):
    return item
