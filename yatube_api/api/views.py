from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Comment, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied()
        serializer.save()

    def perform_destroy(self, instance):
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied()
        instance.delete()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return get_object_or_404(
            Post, pk=self.kwargs.get("post_pk")
        ).comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=self.kwargs.get("post_pk")),
        )

    def perform_update(self, serializer):
        comment = self.get_object()
        if comment.author != self.request.user:
            raise PermissionDenied()
        serializer.save()

    def perform_destroy(self, instance):
        comment = self.get_object()
        if comment.author != self.request.user:
            raise PermissionDenied()
        instance.delete()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
