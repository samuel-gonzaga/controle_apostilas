from django.db import models


# =======================
#        ROLE
# =======================
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# =======================
#        USER
# =======================
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password_hash = models.TextField()
    email = models.EmailField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    created_by = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username


# =======================
#     SOLICITAÇÕES
# =======================
class Solicitacao(models.Model):
    data_pedido = models.DateTimeField()
    apostila = models.CharField(max_length=255)
    nome_aluno = models.CharField(max_length=255)
    dk = models.IntegerField()
    turma = models.CharField(max_length=100)
    horario = models.TimeField()

    impressa = models.BooleanField(default=False)
    entregue = models.BooleanField(default=False)

    data_impressao = models.DateTimeField(null=True, blank=True)
    data_entrega = models.DateTimeField(null=True, blank=True)

    observacoes = models.TextField(blank=True)

    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    arquivado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome_aluno} - {self.apostila}"
