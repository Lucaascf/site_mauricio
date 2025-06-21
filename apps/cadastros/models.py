from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    CodCli = models.CharField(max_length=50, primary_key=True, verbose_name="Código Cliente")
    RazaoSoc = models.TextField(blank=True, null=True, verbose_name="Razão Social")
    End = models.TextField(blank=True, null=True, verbose_name="Endereço")
    Bairro = models.TextField(blank=True, null=True, verbose_name="Bairro")
    Cidade = models.TextField(blank=True, null=True, verbose_name="Cidade")
    Est = models.TextField(blank=True, null=True, verbose_name="Estado")
    Cep = models.TextField(blank=True, null=True, verbose_name="CEP")
    Fone = models.TextField(blank=True, null=True, verbose_name="Telefone")
    Fax = models.TextField(blank=True, null=True, verbose_name="Fax")
    Celular1 = models.TextField(blank=True, null=True, verbose_name="Celular 1")
    Celular2 = models.TextField(blank=True, null=True, verbose_name="Celular 2")
    Cnpj = models.TextField(blank=True, null=True, verbose_name="CNPJ")
    InscRg = models.TextField(blank=True, null=True, verbose_name="Inscrição Estadual")
    Contato1 = models.TextField(blank=True, null=True, verbose_name="Contato 1")
    Contato2 = models.TextField(blank=True, null=True, verbose_name="Contato 2")
    Contato3 = models.TextField(blank=True, null=True, verbose_name="Contato 3")
    Email = models.TextField(blank=True, null=True, verbose_name="Email")
    Informacao = models.TextField(blank=True, null=True, verbose_name="Informações")
    
    class Meta:
        db_table = 'cliente'
        managed = False
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    def __str__(self):
        return f"{self.CodCli} - {self.RazaoSoc or 'N/A'}"


class Fornecedor(models.Model):
    CodFor = models.CharField(max_length=50, primary_key=True, verbose_name="Código Fornecedor")
    RazaoSoc = models.TextField(blank=True, null=True, verbose_name="Razão Social")
    End = models.TextField(blank=True, null=True, verbose_name="Endereço")
    Bairro = models.TextField(blank=True, null=True, verbose_name="Bairro")
    Cidade = models.TextField(blank=True, null=True, verbose_name="Cidade")
    Est = models.TextField(blank=True, null=True, verbose_name="Estado")
    Cep = models.TextField(blank=True, null=True, verbose_name="CEP")
    Fone = models.TextField(blank=True, null=True, verbose_name="Telefone")
    Fax = models.TextField(blank=True, null=True, verbose_name="Fax")
    Celular1 = models.TextField(blank=True, null=True, verbose_name="Celular 1")
    Celular2 = models.TextField(blank=True, null=True, verbose_name="Celular 2")
    Cnpj = models.TextField(blank=True, null=True, verbose_name="CNPJ")
    InscRg = models.TextField(blank=True, null=True, verbose_name="Inscrição Estadual")
    Contato1 = models.TextField(blank=True, null=True, verbose_name="Contato 1")
    Contato2 = models.TextField(blank=True, null=True, verbose_name="Contato 2")
    Contato3 = models.TextField(blank=True, null=True, verbose_name="Contato 3")
    Email = models.TextField(blank=True, null=True, verbose_name="Email")
    Informacao = models.TextField(blank=True, null=True, verbose_name="Informações")
    
    class Meta:
        db_table = 'forneced'
        managed = False
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        
    def __str__(self):
        return f"{self.CodFor} - {self.RazaoSoc or 'N/A'}"


class Produto(models.Model):
    CodProd = models.CharField(max_length=50, primary_key=True, verbose_name="Código Produto")
    Descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    Unid = models.TextField(blank=True, null=True, verbose_name="Unidade")
    Valor = models.TextField(blank=True, null=True, verbose_name="Valor")
    DadosProd = models.TextField(blank=True, null=True, verbose_name="Dados do Produto")
    
    class Meta:
        db_table = 'produto'
        managed = False
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        
    def __str__(self):
        return f"{self.CodProd} - {self.Descricao or 'N/A'}"
    
    def get_valor_decimal(self):
        """Converte o valor text para decimal para exibição"""
        try:
            if self.Valor:
                return float(str(self.Valor).replace(',', '.'))
            return 0.0
        except (ValueError, TypeError):
            return 0.0


class Cotacao(models.Model):
    NumCot = models.AutoField(primary_key=True, verbose_name="Número Cotação")
    DataCot = models.TextField(blank=True, null=True, verbose_name="Data Cotação")
    CodProd = models.TextField(blank=True, null=True, verbose_name="Código Produto")
    CodFor = models.TextField(blank=True, null=True, verbose_name="Código Fornecedor")
    CodCli = models.TextField(blank=True, null=True, verbose_name="Código Cliente")
    Descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    Quant = models.TextField(blank=True, null=True, verbose_name="Quantidade")
    Unid = models.TextField(blank=True, null=True, verbose_name="Unidade")
    Preco = models.TextField(blank=True, null=True, verbose_name="Preço")
    Operador = models.TextField(blank=True, null=True, verbose_name="Operador")
    Respon = models.TextField(blank=True, null=True, verbose_name="Responsável")
    DtFup = models.TextField(blank=True, null=True, verbose_name="Data Follow-up")
    Obs = models.TextField(blank=True, null=True, verbose_name="Observações")
    
    class Meta:
        db_table = 'cotacao'
        managed = False
        verbose_name = 'Cotação'
        verbose_name_plural = 'Cotações'
        
    def __str__(self):
        return f"Cotação {self.NumCot} - {self.CodProd or 'N/A'}"
    
    def get_cliente(self):
        """Retorna o cliente relacionado se existir"""
        if self.CodCli:
            try:
                return Cliente.objects.get(CodCli=self.CodCli)
            except Cliente.DoesNotExist:
                return None
        return None
    
    def get_fornecedor(self):
        """Retorna o fornecedor relacionado se existir"""
        if self.CodFor:
            try:
                return Fornecedor.objects.get(CodFor=self.CodFor)
            except Fornecedor.DoesNotExist:
                return None
        return None
    
    def get_produto(self):
        """Retorna o produto relacionado se existir"""
        if self.CodProd:
            try:
                return Produto.objects.get(CodProd=self.CodProd)
            except Produto.DoesNotExist:
                return None
        return None


class Pedido(models.Model):
    NumPed = models.AutoField(primary_key=True, verbose_name="Número Pedido")
    CodCli = models.TextField(blank=True, null=True, verbose_name="Código Cliente")
    DataPed = models.TextField(blank=True, null=True, verbose_name="Data Pedido")
    CodFor = models.TextField(blank=True, null=True, verbose_name="Código Fornecedor")
    CodProd = models.TextField(blank=True, null=True, verbose_name="Código Produto")
    Descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    Unid = models.TextField(blank=True, null=True, verbose_name="Unidade")
    Quant = models.TextField(blank=True, null=True, verbose_name="Quantidade")
    VrUnit = models.TextField(blank=True, null=True, verbose_name="Valor Unitário")
    VrTot = models.TextField(blank=True, null=True, verbose_name="Valor Total")
    Status = models.TextField(blank=True, null=True, verbose_name="Status")
    Texto = models.TextField(blank=True, null=True, verbose_name="Texto")
    
    class Meta:
        db_table = 'pedido'
        managed = False
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        
    def __str__(self):
        return f"Pedido {self.NumPed} - {self.CodCli or 'N/A'}"
    
    def get_cliente(self):
        """Retorna o cliente relacionado se existir"""
        if self.CodCli:
            try:
                return Cliente.objects.get(CodCli=self.CodCli)
            except Cliente.DoesNotExist:
                return None
        return None
    
    def get_fornecedor(self):
        """Retorna o fornecedor relacionado se existir"""
        if self.CodFor:
            try:
                return Fornecedor.objects.get(CodFor=self.CodFor)
            except Fornecedor.DoesNotExist:
                return None
        return None
    
    def get_produto(self):
        """Retorna o produto relacionado se existir"""
        if self.CodProd:
            try:
                return Produto.objects.get(CodProd=self.CodProd)
            except Produto.DoesNotExist:
                return None
        return None


# TABELAS DE OCORRÊNCIAS

class OcorCli(models.Model):
    id = models.AutoField(primary_key=True)
    CodCli = models.TextField(blank=True, null=True, verbose_name="Código Cliente")
    DtOcor = models.TextField(blank=True, null=True, verbose_name="Data Ocorrência")
    DtFup = models.TextField(blank=True, null=True, verbose_name="Data Follow-up")
    Operador = models.TextField(blank=True, null=True, verbose_name="Operador")
    Respon = models.TextField(blank=True, null=True, verbose_name="Responsável")
    Ocorrencia = models.TextField(blank=True, null=True, verbose_name="Ocorrência")
    
    class Meta:
        db_table = 'ocorcli'
        managed = False
        verbose_name = 'Ocorrência Cliente'
        verbose_name_plural = 'Ocorrências Clientes'
        
    def __str__(self):
        return f"Ocorrência Cliente {self.CodCli or 'N/A'} - {self.DtOcor or 'N/A'}"
    
    def get_cliente(self):
        """Retorna o cliente relacionado se existir"""
        if self.CodCli:
            try:
                return Cliente.objects.get(CodCli=self.CodCli)
            except Cliente.DoesNotExist:
                return None
        return None


class OcorFor(models.Model):
    id = models.AutoField(primary_key=True)
    CodFor = models.TextField(blank=True, null=True, verbose_name="Código Fornecedor")
    DtOcor = models.TextField(blank=True, null=True, verbose_name="Data Ocorrência")
    DtFup = models.TextField(blank=True, null=True, verbose_name="Data Follow-up")
    Operador = models.TextField(blank=True, null=True, verbose_name="Operador")
    Respon = models.TextField(blank=True, null=True, verbose_name="Responsável")
    Ocorrencia = models.TextField(blank=True, null=True, verbose_name="Ocorrência")
    
    class Meta:
        db_table = 'ocorfor'
        managed = False
        verbose_name = 'Ocorrência Fornecedor'
        verbose_name_plural = 'Ocorrências Fornecedores'
        
    def __str__(self):
        return f"Ocorrência Fornecedor {self.CodFor or 'N/A'} - {self.DtOcor or 'N/A'}"
    
    def get_fornecedor(self):
        """Retorna o fornecedor relacionado se existir"""
        if self.CodFor:
            try:
                return Fornecedor.objects.get(CodFor=self.CodFor)
            except Fornecedor.DoesNotExist:
                return None
        return None


class OcorCot(models.Model):
    id = models.AutoField(primary_key=True)
    NumCot = models.TextField(blank=True, null=True, verbose_name="Número Cotação")
    CodFor = models.TextField(blank=True, null=True, verbose_name="Código Fornecedor")
    CodProd = models.TextField(blank=True, null=True, verbose_name="Código Produto")
    DtOcor = models.TextField(blank=True, null=True, verbose_name="Data Ocorrência")
    Operador = models.TextField(blank=True, null=True, verbose_name="Operador")
    Respon = models.TextField(blank=True, null=True, verbose_name="Responsável")
    DtFup = models.TextField(blank=True, null=True, verbose_name="Data Follow-up")
    Texto = models.TextField(blank=True, null=True, verbose_name="Texto")
    
    class Meta:
        db_table = 'ocorcot'
        managed = False
        verbose_name = 'Ocorrência Cotação'
        verbose_name_plural = 'Ocorrências Cotações'
        
    def __str__(self):
        return f"Ocorrência Cotação {self.NumCot or 'N/A'} - {self.DtOcor or 'N/A'}"
    
    def get_cotacao(self):
        """Retorna a cotação relacionada se existir"""
        if self.NumCot:
            try:
                return Cotacao.objects.get(NumCot=self.NumCot)
            except Cotacao.DoesNotExist:
                return None
        return None
    
    def get_fornecedor(self):
        """Retorna o fornecedor relacionado se existir"""
        if self.CodFor:
            try:
                return Fornecedor.objects.get(CodFor=self.CodFor)
            except Fornecedor.DoesNotExist:
                return None
        return None
    
    def get_produto(self):
        """Retorna o produto relacionado se existir"""
        if self.CodProd:
            try:
                return Produto.objects.get(CodProd=self.CodProd)
            except Produto.DoesNotExist:
                return None
        return None


class OcorPedC(models.Model):
    id = models.AutoField(primary_key=True)
    NumPed = models.TextField(blank=True, null=True, verbose_name="Número Pedido")
    CodCli = models.TextField(blank=True, null=True, verbose_name="Código Cliente")
    DtOcor = models.TextField(blank=True, null=True, verbose_name="Data Ocorrência")
    DtFup = models.TextField(blank=True, null=True, verbose_name="Data Follow-up")
    Operador = models.TextField(blank=True, null=True, verbose_name="Operador")
    Respon = models.TextField(blank=True, null=True, verbose_name="Responsável")
    DataPed = models.TextField(blank=True, null=True, verbose_name="Data Pedido")
    Ocorrencia = models.TextField(blank=True, null=True, verbose_name="Ocorrência")
    
    class Meta:
        db_table = 'ocorpedc'
        managed = False
        verbose_name = 'Ocorrência Pedido Cliente'
        verbose_name_plural = 'Ocorrências Pedidos Clientes'
        
    def __str__(self):
        return f"Ocorrência Pedido {self.NumPed or 'N/A'} - Cliente {self.CodCli or 'N/A'}"
    
    def get_pedido(self):
        """Retorna o pedido relacionado se existir"""
        if self.NumPed:
            try:
                return Pedido.objects.get(NumPed=self.NumPed)
            except (Pedido.DoesNotExist, ValueError):
                return None
        return None
    
    def get_cliente(self):
        """Retorna o cliente relacionado se existir"""
        if self.CodCli:
            try:
                return Cliente.objects.get(CodCli=self.CodCli)
            except Cliente.DoesNotExist:
                return None
        return None


class OcorPedF(models.Model):
    id = models.AutoField(primary_key=True)
    NumPed = models.TextField(blank=True, null=True, verbose_name="Número Pedido")
    CodCli = models.TextField(blank=True, null=True, verbose_name="Código Cliente")
    CodFor = models.TextField(blank=True, null=True, verbose_name="Código Fornecedor")
    DtOcor = models.TextField(blank=True, null=True, verbose_name="Data Ocorrência")
    DtFup = models.TextField(blank=True, null=True, verbose_name="Data Follow-up")
    Operador = models.TextField(blank=True, null=True, verbose_name="Operador")
    Respon = models.TextField(blank=True, null=True, verbose_name="Responsável")
    DataPed = models.TextField(blank=True, null=True, verbose_name="Data Pedido")
    Ocorrencia = models.TextField(blank=True, null=True, verbose_name="Ocorrência")
    
    class Meta:
        db_table = 'ocorpedf'
        managed = False
        verbose_name = 'Ocorrência Pedido Fornecedor'
        verbose_name_plural = 'Ocorrências Pedidos Fornecedores'
        
    def __str__(self):
        return f"Ocorrência Pedido {self.NumPed or 'N/A'} - Fornecedor {self.CodFor or 'N/A'}"
    
    def get_pedido(self):
        """Retorna o pedido relacionado se existir"""
        if self.NumPed:
            try:
                return Pedido.objects.get(NumPed=self.NumPed)
            except (Pedido.DoesNotExist, ValueError):
                return None
        return None
    
    def get_cliente(self):
        """Retorna o cliente relacionado se existir"""
        if self.CodCli:
            try:
                return Cliente.objects.get(CodCli=self.CodCli)
            except Cliente.DoesNotExist:
                return None
        return None
    
    def get_fornecedor(self):
        """Retorna o fornecedor relacionado se existir"""
        if self.CodFor:
            try:
                return Fornecedor.objects.get(CodFor=self.CodFor)
            except Fornecedor.DoesNotExist:
                return None
        return None
    

class Usuario(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome")
    email = models.EmailField(unique=True, verbose_name="Email")
    senha = models.CharField(max_length=128, verbose_name="Senha")
    
    class Meta:
        db_table = 'usuario'
        managed = False  # Se quiser que o Django não gerencie a tabela
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        
    def __str__(self):
        return f"{self.nome} ({self.email})"