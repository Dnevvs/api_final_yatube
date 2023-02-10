from django.core.exceptions import BadRequest, PermissionDenied
from django.shortcuts import get_object_or_404
from posts.models import Comment, Follow, Group, Post, User
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.throttling import ScopedRateThrottle

from .permissions import OwnerOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from .throttling import WorkingHoursRateThrottle


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    throttle_classes = (WorkingHoursRateThrottle, ScopedRateThrottle)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        if serializer.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super(PostViewSet, self).perform_destroy(serializer)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(
            author=self.request.user, post=post)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        if serializer.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super(CommentViewSet, self).perform_destroy(serializer)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GetPostViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass


class FollowViewSet(GetPostViewSet):
    serializer_class = FollowSerializer
    permission_classes = (OwnerOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', )

    def perform_create(self, serializer):
        if not self.request.data or not self.request.data['following']:
            raise BadRequest('Пустой запрос')
        following = get_object_or_404(
            User, username=self.request.data['following'])
        follows = Follow.objects.filter(user=self.request.user,
                                        following=following)
        if follows:
            raise BadRequest('Повторная подписка невозможна')
        if following == self.request.user:
            raise BadRequest('Подписка на себя невозможна')
        serializer.save(user=self.request.user, following=following)

    def get_queryset(self):
        new_queryset = Follow.objects.filter(user=self.request.user)
        return new_queryset
