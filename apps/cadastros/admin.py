from django.contrib import admin
from .models import (
    Cliente, Fornecedor, Produto, Cotacao, Pedido,
    OcorCli, OcorFor, OcorCot, OcorPedC, OcorPedF, Usuario
)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['CodCli', 'RazaoSoc', 'Cidade', 'Est', 'Fone', 'Email']
    list_filter = ['Est', 'Cidade']
    search_fields = ['CodCli', 'RazaoSoc', 'Cnpj', 'Email', 'Cidade']
    list_per_page = 50
    
    fieldsets = (
        ('Identificação', {
            'fields': ('CodCli', 'RazaoSoc', 'Cnpj', 'InscRg')
        }),
        ('Endereço', {
            'fields': ('End', 'Bairro', 'Cidade', 'Est', 'Cep')
        }),
        ('Contato', {
            'fields': ('Fone', 'Fax', 'Celular1', 'Celular2', 'Email')
        }),
        ('Pessoas de Contato', {
            'fields': ('Contato1', 'Contato2', 'Contato3')
        }),
        ('Informações Adicionais', {
            'fields': ('Informacao',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['CodFor', 'RazaoSoc', 'Cidade', 'Est', 'Fone', 'Email']
    list_filter = ['Est', 'Cidade']
    search_fields = ['CodFor', 'RazaoSoc', 'Cnpj', 'Email', 'Cidade']
    list_per_page = 50
    
    fieldsets = (
        ('Identificação', {
            'fields': ('CodFor', 'RazaoSoc', 'Cnpj', 'InscRg')
        }),
        ('Endereço', {
            'fields': ('End', 'Bairro', 'Cidade', 'Est', 'Cep')
        }),
        ('Contato', {
            'fields': ('Fone', 'Fax', 'Celular1', 'Celular2', 'Email')
        }),
        ('Pessoas de Contato', {
            'fields': ('Contato1', 'Contato2', 'Contato3')
        }),
        ('Informações Adicionais', {
            'fields': ('Informacao',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['CodProd', 'Descricao', 'Unid', 'get_valor_display']
    list_filter = ['Unid']
    search_fields = ['CodProd', 'Descricao']
    list_per_page = 50
    
    fieldsets = (
        ('Informações do Produto', {
            'fields': ('CodProd', 'Descricao', 'Unid', 'Valor', 'DadosProd')
        }),
    )
    
    def get_valor_display(self, obj):
        """Exibe o valor formatado"""
        return f"R$ {obj.get_valor_decimal():,.2f}" if obj.get_valor_decimal() else "R$ 0,00"
    get_valor_display.short_description = 'Valor'


@admin.register(Cotacao)
class CotacaoAdmin(admin.ModelAdmin):
    list_display = ['NumCot', 'DataCot', 'CodCli', 'CodFor', 'CodProd', 'Descricao', 'Preco', 'Operador']
    list_filter = ['DataCot', 'Operador', 'Respon']
    search_fields = ['NumCot', 'CodCli', 'CodFor', 'CodProd', 'Descricao']
    list_per_page = 50
    ordering = ['-NumCot']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('NumCot', 'DataCot', 'Operador', 'Respon')
        }),
        ('Relacionamentos', {
            'fields': ('CodCli', 'CodFor', 'CodProd')
        }),
        ('Detalhes do Produto', {
            'fields': ('Descricao', 'Quant', 'Unid', 'Preco')
        }),
        ('Controle', {
            'fields': ('DtFup', 'Obs'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['NumCot']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['NumPed', 'DataPed', 'CodCli', 'CodFor', 'CodProd', 'Descricao', 'VrTot', 'Status']
    list_filter = ['DataPed', 'Status']
    search_fields = ['NumPed', 'CodCli', 'CodFor', 'CodProd', 'Descricao']
    list_per_page = 50
    ordering = ['-NumPed']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('NumPed', 'DataPed', 'Status')
        }),
        ('Relacionamentos', {
            'fields': ('CodCli', 'CodFor', 'CodProd')
        }),
        ('Detalhes do Produto', {
            'fields': ('Descricao', 'Quant', 'Unid', 'VrUnit', 'VrTot')
        }),
        ('Observações', {
            'fields': ('Texto',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['NumPed']


# ADMINISTRAÇÃO DAS OCORRÊNCIAS

@admin.register(OcorCli)
class OcorCliAdmin(admin.ModelAdmin):
    list_display = ['id', 'CodCli', 'DtOcor', 'DtFup', 'Operador', 'Respon', 'ocorrencia_resumo']
    list_filter = ['DtOcor', 'Operador', 'Respon']
    search_fields = ['CodCli', 'Operador', 'Respon', 'Ocorrencia']
    list_per_page = 50
    ordering = ['-DtOcor']
    
    fieldsets = (
        ('Identificação', {
            'fields': ('CodCli', 'DtOcor', 'DtFup')
        }),
        ('Responsáveis', {
            'fields': ('Operador', 'Respon')
        }),
        ('Ocorrência', {
            'fields': ('Ocorrencia',)
        }),
    )
    
    def ocorrencia_resumo(self, obj):
        """Exibe um resumo da ocorrência"""
        if obj.Ocorrencia:
            return obj.Ocorrencia[:50] + "..." if len(obj.Ocorrencia) > 50 else obj.Ocorrencia
        return "Sem descrição"
    ocorrencia_resumo.short_description = 'Resumo Ocorrência'


@admin.register(OcorFor)
class OcorForAdmin(admin.ModelAdmin):
    list_display = ['id', 'CodFor', 'DtOcor', 'DtFup', 'Operador', 'Respon', 'ocorrencia_resumo']
    list_filter = ['DtOcor', 'Operador', 'Respon']
    search_fields = ['CodFor', 'Operador', 'Respon', 'Ocorrencia']
    list_per_page = 50
    ordering = ['-DtOcor']
    
    fieldsets = (
        ('Identificação', {
            'fields': ('CodFor', 'DtOcor', 'DtFup')
        }),
        ('Responsáveis', {
            'fields': ('Operador', 'Respon')
        }),
        ('Ocorrência', {
            'fields': ('Ocorrencia',)
        }),
    )
    
    def ocorrencia_resumo(self, obj):
        """Exibe um resumo da ocorrência"""
        if obj.Ocorrencia:
            return obj.Ocorrencia[:50] + "..." if len(obj.Ocorrencia) > 50 else obj.Ocorrencia
        return "Sem descrição"
    ocorrencia_resumo.short_description = 'Resumo Ocorrência'


@admin.register(OcorCot)
class OcorCotAdmin(admin.ModelAdmin):
    list_display = ['id', 'NumCot', 'CodFor', 'CodProd', 'DtOcor', 'Operador', 'Respon', 'texto_resumo']
    list_filter = ['DtOcor', 'Operador', 'Respon']
    search_fields = ['NumCot', 'CodFor', 'CodProd', 'Operador', 'Texto']
    list_per_page = 50
    ordering = ['-DtOcor']
    
    fieldsets = (
        ('Identificação', {
            'fields': ('NumCot', 'CodFor', 'CodProd', 'DtOcor', 'DtFup')
        }),
        ('Responsáveis', {
            'fields': ('Operador', 'Respon')
        }),
        ('Texto', {
            'fields': ('Texto',)
        }),
    )
    
    def texto_resumo(self, obj):
        """Exibe um resumo do texto"""
        if obj.Texto:
            return obj.Texto[:50] + "..." if len(obj.Texto) > 50 else obj.Texto
        return "Sem texto"
    texto_resumo.short_description = 'Resumo Texto'


@admin.register(OcorPedC)
class OcorPedCAdmin(admin.ModelAdmin):
    list_display = ['id', 'NumPed', 'CodCli', 'DataPed', 'DtOcor', 'DtFup', 'Operador', 'Respon']
    list_filter = ['DtOcor', 'DataPed', 'Operador', 'Respon']
    search_fields = ['NumPed', 'CodCli', 'Operador', 'Respon', 'Ocorrencia']
    list_per_page = 50
    ordering = ['-DtOcor']
    
    fieldsets = (
        ('Identificação', {
            'fields': ('NumPed', 'CodCli', 'DataPed')
        }),
        ('Datas', {
            'fields': ('DtOcor', 'DtFup')
        }),
        ('Responsáveis', {
            'fields': ('Operador', 'Respon')
        }),
        ('Ocorrência', {
            'fields': ('Ocorrencia',)
        }),
    )


@admin.register(OcorPedF)
class OcorPedFAdmin(admin.ModelAdmin):
    list_display = ['id', 'NumPed', 'CodCli', 'CodFor', 'DataPed', 'DtOcor', 'DtFup', 'Operador', 'Respon']
    list_filter = ['DtOcor', 'DataPed', 'Operador', 'Respon']
    search_fields = ['NumPed', 'CodCli', 'CodFor', 'Operador', 'Respon', 'Ocorrencia']
    list_per_page = 50
    ordering = ['-DtOcor']
    
    fieldsets = (
        ('Identificação', {
            'fields': ('NumPed', 'CodCli', 'CodFor', 'DataPed')
        }),
        ('Datas', {
            'fields': ('DtOcor', 'DtFup')
        }),
        ('Responsáveis', {
            'fields': ('Operador', 'Respon')
        }),
        ('Ocorrência', {
            'fields': ('Ocorrencia',)
        }),
    )

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email']
    search_fields = ['nome', 'email']
    
    fieldsets = (
        ('Dados do Usuário', {
            'fields': ('nome', 'email', 'senha')
        }),
    )