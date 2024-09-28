# -*- coding: utf-8 -*-
from blog.ninjia import router


@router.get("/posts")
def list_posts(request):
    return {"posts": ["Post 1", "Post 2"]}
