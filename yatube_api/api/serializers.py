from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "text",
            "author",
            "image",
            "group",
            "pub_date",
        )
        read_only_fields = ("pub_date",)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "text", "author", "post", "created")
        read_only_fields = ("created", "author", "post")
