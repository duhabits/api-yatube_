from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_main = DefaultRouter('v1')
router_main.register("posts", PostViewSet)
router_main.register("groups", GroupViewSet)
router_comment = routers.NestedSimpleRouter(
    router_main, "posts", lookup="post"
)
router_comment.register("comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("v1/", include(router_main.urls)),
    path("v1/", include(router_comment.urls)),
    path("v1/api-token-auth/", views.obtain_auth_token),
]
