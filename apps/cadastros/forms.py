from django import forms
from .models import Cliente, Fornecedor, Produto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['CodCli', 'RazaoSoc', 'Cnpj', 'InscRg', 'End', 'Bairro', 
                 'Cidade', 'Est', 'Cep', 'Fone', 'Fax', 'Celular1', 'Celular2', 
                 'Email', 'Contato1', 'Contato2', 'Contato3', 'Informacao']
        
        widgets = {
            'CodCli': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código do cliente'}),
            'RazaoSoc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo da empresa'}),
            'Cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CNPJ'}),
            'InscRg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inscrição Estadual'}),
            'End': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço completo'}),
            'Bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'Cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'Est': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
            'Cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'Fone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'Fax': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fax'}),
            'Celular1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular 1'}),
            'Celular2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular 2'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'Contato1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do contato'}),
            'Contato2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do contato'}),
            'Contato3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do contato'}),
            'Informacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Informações adicionais sobre o cliente...'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Se é edição (instance existe), torna o campo CodCli readonly
        if self.instance and self.instance.pk:
            self.fields['CodCli'].widget.attrs['readonly'] = True
            self.fields['CodCli'].widget.attrs['class'] += ' bg-light'
            self.fields['CodCli'].help_text = 'O código do cliente não pode ser alterado após a criação.'
    
    def clean_CodCli(self):
        codigo = self.cleaned_data.get('CodCli')
        if not codigo:
            raise forms.ValidationError('Código do cliente é obrigatório.')
        
        # Se é edição, retorna o código original (não permite alteração)
        if self.instance and self.instance.pk:
            return self.instance.CodCli
            
        return codigo.upper()

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['CodFor', 'RazaoSoc', 'Cnpj', 'InscRg', 'End', 'Bairro', 
                 'Cidade', 'Est', 'Cep', 'Fone', 'Fax', 'Celular1', 'Celular2', 
                 'Email', 'Contato1', 'Contato2', 'Contato3']
        
        widgets = {
            'CodFor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código do fornecedor'}),
            'RazaoSoc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo da empresa'}),
            'Cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CNPJ'}),
            'InscRg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inscrição Estadual'}),
            'End': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço completo'}),
            'Bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'Cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'Est': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
            'Cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'Fone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'Fax': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fax'}),
            'Celular1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular 1'}),
            'Celular2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular 2'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'Contato1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do contato'}),
            'Contato2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do contato'}),
            'Contato3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do contato'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Se é edição (instance existe), torna o campo CodFor readonly
        if self.instance and self.instance.pk:
            self.fields['CodFor'].widget.attrs['readonly'] = True
            self.fields['CodFor'].widget.attrs['class'] += ' bg-light'
            self.fields['CodFor'].help_text = 'O código do fornecedor não pode ser alterado após a criação.'
    
    def clean_CodFor(self):
        codigo = self.cleaned_data.get('CodFor')
        if not codigo:
            raise forms.ValidationError('Código do fornecedor é obrigatório.')
        
        # Se é edição, retorna o código original (não permite alteração)
        if self.instance and self.instance.pk:
            return self.instance.CodFor
            
        return codigo.upper()
    
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['CodProd', 'Descricao', 'Unid', 'Valor', 'DadosProd']
        
        widgets = {
            'CodProd': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex: PROD001'
            }),
            'Descricao': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Descrição do produto'
            }),
            'Unid': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'UN, KG, M², L, etc.'
            }),
            'Valor': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '0,00'
            }),
            'DadosProd': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4,
                'placeholder': 'Informações técnicas, especificações, observações sobre o produto...'
            }),
        }
    
    def clean_CodProd(self):
        codigo = self.cleaned_data.get('CodProd')
        if not codigo:
            raise forms.ValidationError('Código do produto é obrigatório.')
        return codigo.upper().strip()
    
    def clean_Descricao(self):
        descricao = self.cleaned_data.get('Descricao')
        if descricao:
            return descricao.strip()
        return descricao
    
    def clean_Valor(self):
        valor = self.cleaned_data.get('Valor')
        if valor:
            # Remove formatação e converte para formato de banco
            valor = str(valor).replace('.', '').replace(',', '.')
            try:
                float(valor)
                return valor
            except ValueError:
                raise forms.ValidationError('Valor deve ser um número válido.')
        return valor