# -*- coding: utf-8 -*-
from ninja import NinjaAPI

from blog.ninjia import router as blog_router
from users.ninjia import router as users_router

ninja_api = NinjaAPI(
    title="测试 API",  # 自定义标题
    description="This is a detailed description of my API.",  # 自定义描述
    version="1.0.0"  # 自定义版本
)
# ninja_api.add_router("/blog/", blog_router)
ninja_api.add_router("/users/", users_router)
