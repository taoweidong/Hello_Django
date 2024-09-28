from ninja_extra import api_controller, ControllerBase, http_get

from blog.ninjia import router


# Create your views here.
@router.get("/posts")
def list_posts(request):
    return {"posts": ["Post 1", "Post 2"]}


@api_controller("/app2", tags=["blog"])
class App2Controller(ControllerBase):

    @http_get("/hello")
    def hello_app2(self, request):
        return {"message": "Hello from App2!"}
