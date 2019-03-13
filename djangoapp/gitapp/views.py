from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from djangoapp.gitapp.models import User, Repository
from djangoapp.gitapp.serializers import UserSerializer, RepositorySerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('user_type', )


class RepositoryView(ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
