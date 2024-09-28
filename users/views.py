# -*- coding: utf-8 -*-

from users.ninjia import router


@router.get("/list")
def list_users(request):
    return {"users": ["User 1", "User 2"]}
