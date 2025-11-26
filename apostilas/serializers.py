from rest_framework import serializers
from .models import Role, User, Solicitacao


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        source='role',
        write_only=True
    )

    created_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False
    )

    class Meta:
        model = User
        fields = [
            'id', 'username', 'password_hash', 'email',
            'created_at', 'role', 'role_id', 'created_by'
        ]


class SolicitacaoSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    created_by_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='created_by',
        write_only=True
    )

    class Meta:
        model = Solicitacao
        fields = '__all__'
