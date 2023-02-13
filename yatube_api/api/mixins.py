from rest_framework import mixins, viewsets


class GetPostViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass
