import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_comercial.settings')
django.setup()

from django.db import connection
from apps.cadastros.models import Cliente, Fornecedor, Produto

# 1. Verificar conexão com MySQL
print("=== CONEXÃO COM BANCO ===")
with connection.cursor() as cursor:
    cursor.execute("SELECT DATABASE();")
    result = cursor.fetchone()
    print(f"Banco conectado: {result[0]}")

# 2. Listar tabelas no banco
print("\n=== TABELAS NO BANCO ===")
with connection.cursor() as cursor:
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    for table in tables:
        print(f"- {table[0]}")

# 3. Verificar estrutura da tabela clientes (se existir)
print("\n=== ESTRUTURA TABELA CLIENTES ===")
with connection.cursor() as cursor:
    try:
        cursor.execute("DESCRIBE clientes;")  # ou qualquer nome que seja sua tabela
        columns = cursor.fetchall()
        for col in columns:
            print(f"- {col[0]} ({col[1]})")
    except Exception as e:
        print(f"Erro ao descrever tabela 'clientes': {e}")
        
        # Tentar outros nomes possíveis
        possible_names = ['cliente', 'cadastros_cliente', 'tb_clientes', 'tbl_clientes']
        for name in possible_names:
            try:
                cursor.execute(f"DESCRIBE {name};")
                print(f"Tabela encontrada: {name}")
                columns = cursor.fetchall()
                for col in columns:
                    print(f"- {col[0]} ({col[1]})")
                break
            except:
                continue

# 4. Contar registros diretamente no SQL
print("\n=== CONTAGEM DIRETA NO SQL ===")
with connection.cursor() as cursor:
    try:
        cursor.execute("SELECT COUNT(*) FROM clientes;")
        count = cursor.fetchone()[0]
        print(f"Registros na tabela clientes: {count}")
    except Exception as e:
        print(f"Erro ao contar clientes: {e}")

# 5. Tentar via Django ORM
print("\n=== VIA DJANGO ORM ===")
try:
    count = Cliente.objects.count()
    print(f"Clientes via ORM: {count}")
except Exception as e:
    print(f"Erro no ORM: {e}")