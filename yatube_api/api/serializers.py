import base64

from django.core.files.base import ContentFile
from posts.models import Comment, Follow, Group, Post
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group

    def __str__(self):
        return f'{self.slug}'


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    group = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Group.objects.all())
    comments = serializers.PrimaryKeyRelatedField(
        required=False, many=True, queryset=Comment.objects.all())
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = ('id',
                  'text', 'author', 'image', 'pub_date', 'group', 'comments')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    following = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('user', 'following')
        model = Follow
