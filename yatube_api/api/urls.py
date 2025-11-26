from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_main = DefaultRouter()
router_main.register("posts", PostViewSet)
router_main.register("groups", GroupViewSet)
router_main.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
urlpatterns = [
    path("v1/", include(router_main.urls)),
    path("v1/api-token-auth/", views.obtain_auth_token),
]
