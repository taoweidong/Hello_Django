# -*- coding: utf-8 -*-
from ninja_extra import api_controller, ControllerBase, http_get

from users.ninjia import router


@router.get("/users")
def list_users(request):
    return {"users": ["User 1", "User 2"]}


@api_controller("/app2", tags=["users"])
class AppUserController(ControllerBase):

    @http_get("/hello")
    def hello_app2(self, request):
        return {"message": "Hello from App2!"}
