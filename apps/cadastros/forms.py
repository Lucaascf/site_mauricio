from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
from .models import Cliente, Fornecedor, Produto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['CodCli', 'RazaoSoc', 'Cnpj', 'InscRg', 'End', 'Bairro', 
                 'Cidade', 'Est', 'Cep', 'Fone', 'Fax', 'Celular1', 'Celular2', 
                 'Email', 'Contato1', 'Contato2', 'Contato3', 'Informacao']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('CodCli', css_class='form-group col-md-4 mb-0'),
                Column('RazaoSoc', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Cnpj', css_class='form-group col-md-6 mb-0'),
                Column('InscRg', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('End', css_class='form-group col-md-8 mb-0'),
                Column('Bairro', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Cidade', css_class='form-group col-md-6 mb-0'),
                Column('Est', css_class='form-group col-md-2 mb-0'),
                Column('Cep', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Fone', css_class='form-group col-md-4 mb-0'),
                Column('Fax', css_class='form-group col-md-4 mb-0'),
                Column('Email', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Celular1', css_class='form-group col-md-6 mb-0'),
                Column('Celular2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Contato1', css_class='form-group col-md-4 mb-0'),
                Column('Contato2', css_class='form-group col-md-4 mb-0'),
                Column('Contato3', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'Informacao',
            Submit('submit', 'Salvar', css_class='btn btn-primary')
        )

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['CodFor', 'RazaoSoc', 'Cnpj', 'InscRg', 'End', 'Bairro', 
                 'Cidade', 'Est', 'Cep', 'Fone', 'Fax', 'Celular1', 'Celular2', 
                 'Email', 'Contato1', 'Contato2', 'Contato3']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('CodFor', css_class='form-group col-md-4 mb-0'),
                Column('RazaoSoc', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Cnpj', css_class='form-group col-md-6 mb-0'),
                Column('InscRg', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('End', css_class='form-group col-md-8 mb-0'),
                Column('Bairro', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Cidade', css_class='form-group col-md-6 mb-0'),
                Column('Est', css_class='form-group col-md-2 mb-0'),
                Column('Cep', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Fone', css_class='form-group col-md-4 mb-0'),
                Column('Fax', css_class='form-group col-md-4 mb-0'),
                Column('Email', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Celular1', css_class='form-group col-md-6 mb-0'),
                Column('Celular2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Contato1', css_class='form-group col-md-4 mb-0'),
                Column('Contato2', css_class='form-group col-md-4 mb-0'),
                Column('Contato3', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Salvar', css_class='btn btn-success')
        )

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['CodProd', 'Descricao', 'Unid', 'Valor']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('CodProd', css_class='form-group col-md-4 mb-0'),
                Column('Descricao', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Unid', css_class='form-group col-md-6 mb-0'),
                Column('Valor', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Salvar', css_class='btn btn-info')
        )