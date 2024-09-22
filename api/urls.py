from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from .api import ninja_api
from .book_views import book_api
from .views import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='API 接口文档')),
    path("api/", ninja_api.urls),
    # path("book_api/", book_api.urls),
]
