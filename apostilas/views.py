from rest_framework import viewsets
from .models import Role, User, Solicitacao
from .serializers import RoleSerializer, UserSerializer, SolicitacaoSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer
