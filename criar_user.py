from apps.cadastros.models import Cliente, Fornecedor, Produto, Usuario

# Criar um usuário
usuario = Usuario.objects.create(
    nome='Admin',
    email='admin@empresa.com',
    senha='123456'
)
print(f"Usuário criado: {usuario}")
