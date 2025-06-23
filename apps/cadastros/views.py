from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q
from django.db import transaction
from .models import Cliente, Fornecedor, Produto
from .forms import ClienteForm, FornecedorForm, ProdutoForm

# ============= VIEWS CLIENTES =============

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'cadastros/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = Cliente.objects.all()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(CodCli__icontains=search) |
                Q(RazaoSoc__icontains=search) |
                Q(Cnpj__icontains=search) |
                Q(Cidade__icontains=search) |
                Q(Email__icontains=search) |
                Q(Fone__icontains=search) |
                Q(Celular1__icontains=search)
            )
        return queryset.order_by('CodCli')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['total_clientes'] = Cliente.objects.count()
        return context


class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'cadastros/cliente_detail.html'
    context_object_name = 'cliente'
    pk_url_kwarg = 'pk'
    
    def get_object(self, queryset=None):
        """Override para buscar pelo CodCli que é a primary key string"""
        if queryset is None:
            queryset = self.get_queryset()
        
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            try:
                return queryset.get(CodCli=pk)
            except Cliente.DoesNotExist:
                from django.http import Http404
                raise Http404(f"Cliente com código '{pk}' não encontrado.")
        
        raise AttributeError("ClienteDetailView deve ser chamado com um pk.")


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cadastros/cliente_form.html'
    success_url = reverse_lazy('cadastros:cliente_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Novo Cliente'
        context['action'] = 'Criar'
        return context
    
    def form_valid(self, form):
        print(f"=== CLIENTE CREATE - FORM VÁLIDO ===")
        try:
            with transaction.atomic():
                # Verificar se o código já existe
                codigo = form.cleaned_data['CodCli'].upper().strip()
                print(f"=== VERIFICANDO CÓDIGO: {codigo} ===")
                
                if Cliente.objects.filter(CodCli=codigo).exists():
                    print(f"=== CÓDIGO JÁ EXISTE: {codigo} ===")
                    messages.error(self.request, f'Cliente com código "{codigo}" já existe!')
                    return self.form_invalid(form)
                
                # Limpar campos vazios
                instance = form.save(commit=False)
                instance.CodCli = codigo
                
                # Converter strings vazias para None
                for field in instance._meta.fields:
                    if field.name not in ['CodCli', 'RazaoSoc']:
                        value = getattr(instance, field.name)
                        if value == '':
                            setattr(instance, field.name, None)
                
                print(f"=== SALVANDO CLIENTE: {instance.CodCli} - {instance.RazaoSoc} ===")
                instance.save()
                
                # Verificar se foi salvo
                cliente_salvo = Cliente.objects.get(CodCli=codigo)
                print(f"=== CONFIRMAÇÃO: Cliente salvo no banco: {cliente_salvo.RazaoSoc} ===")
                
                messages.success(self.request, f'Cliente "{codigo} - {instance.RazaoSoc}" criado com sucesso!')
                return super().form_valid(form)
                
        except Exception as e:
            print(f"=== ERRO AO SALVAR: {str(e)} ===")
            import traceback
            print(f"=== TRACEBACK: {traceback.format_exc()} ===")
            messages.error(self.request, f'Erro ao criar cliente: {str(e)}')
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        print(f"=== FORM INVÁLIDO ===")
        for field, errors in form.errors.items():
            print(f"{field}: {errors}")
        messages.error(self.request, 'Por favor, corrija os erros abaixo.')
        return super().form_invalid(form)


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cadastros/cliente_form.html'
    pk_url_kwarg = 'pk'
    
    def get_object(self, queryset=None):
        """Override para buscar pelo CodCli"""
        if queryset is None:
            queryset = self.get_queryset()
        
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            try:
                return queryset.get(CodCli=pk)
            except Cliente.DoesNotExist:
                from django.http import Http404
                raise Http404(f"Cliente com código '{pk}' não encontrado.")
        
        raise AttributeError("ClienteUpdateView deve ser chamado com um pk.")
    
    def get_success_url(self):
        return reverse_lazy('cadastros:cliente_detail', kwargs={'pk': self.object.CodCli})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar Cliente - {self.object.CodCli}'
        context['action'] = 'Atualizar'
        context['cliente'] = self.object
        return context
    
    def form_valid(self, form):
        try:
            messages.success(self.request, f'Cliente "{self.object.CodCli}" atualizado com sucesso!')
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f'Erro ao atualizar cliente: {str(e)}')
            return self.form_invalid(form)


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'cadastros/cliente_confirm_delete.html'
    success_url = reverse_lazy('cadastros:cliente_list')
    context_object_name = 'cliente'
    pk_url_kwarg = 'pk'
    
    def get_object(self, queryset=None):
        """Override para buscar pelo CodCli"""
        if queryset is None:
            queryset = self.get_queryset()
        
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            try:
                return queryset.get(CodCli=pk)
            except Cliente.DoesNotExist:
                from django.http import Http404
                raise Http404(f"Cliente com código '{pk}' não encontrado.")
        
        raise AttributeError("ClienteDeleteView deve ser chamado com um pk.")
    
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            messages.success(request, f'Cliente "{self.object.CodCli}" excluído com sucesso!')
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            messages.error(request, f'Erro ao excluir cliente: {str(e)}')
            return redirect('cadastros:cliente_detail', pk=self.object.CodCli)


# ============= VIEWS FORNECEDORES =============

class FornecedorListView(LoginRequiredMixin, ListView):
    model = Fornecedor
    template_name = 'cadastros/fornecedor_list.html'
    context_object_name = 'fornecedores'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = Fornecedor.objects.all()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(CodFor__icontains=search) |
                Q(RazaoSoc__icontains=search) |
                Q(Cnpj__icontains=search) |
                Q(Cidade__icontains=search) |
                Q(Email__icontains=search) |
                Q(Fone__icontains=search)
            )
        return queryset.order_by('CodFor')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['total_fornecedores'] = Fornecedor.objects.count()
        return context


class FornecedorDetailView(LoginRequiredMixin, DetailView):
    model = Fornecedor
    template_name = 'cadastros/fornecedor_detail.html'
    context_object_name = 'fornecedor'
    pk_url_kwarg = 'pk'
    
    def get_object(self, queryset=None):
        """Override para buscar pelo CodFor"""
        if queryset is None:
            queryset = self.get_queryset()
        
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            try:
                return queryset.get(CodFor=pk)
            except Fornecedor.DoesNotExist:
                from django.http import Http404
                raise Http404(f"Fornecedor com código '{pk}' não encontrado.")
        
        raise AttributeError("FornecedorDetailView deve ser chamado com um pk.")


class FornecedorCreateView(LoginRequiredMixin, CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'cadastros/fornecedor_form.html'
    success_url = reverse_lazy('cadastros:fornecedor_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Novo Fornecedor'
        context['action'] = 'Criar'
        return context
    
    def form_valid(self, form):
        try:
            codigo = form.cleaned_data['CodFor'].upper().strip()
            if Fornecedor.objects.filter(CodFor=codigo).exists():
                messages.error(self.request, f'Fornecedor com código "{codigo}" já existe!')
                return self.form_invalid(form)
            
            instance = form.save(commit=False)
            instance.CodFor = codigo
            instance.save()
            
            messages.success(self.request, f'Fornecedor "{codigo}" criado com sucesso!')
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f'Erro ao criar fornecedor: {str(e)}')
            return self.form_invalid(form)


class FornecedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'cadastros/fornecedor_form.html'
    pk_url_kwarg = 'pk'
    
    def get_object(self, queryset=None):
        """Override para buscar pelo CodFor"""
        if queryset is None:
            queryset = self.get_queryset()
        
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            try:
                return queryset.get(CodFor=pk)
            except Fornecedor.DoesNotExist:
                from django.http import Http404
                raise Http404(f"Fornecedor com código '{pk}' não encontrado.")
        
        raise AttributeError("FornecedorUpdateView deve ser chamado com um pk.")
    
    def get_success_url(self):
        return reverse_lazy('cadastros:fornecedor_detail', kwargs={'pk': self.object.CodFor})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar Fornecedor - {self.object.CodFor}'
        context['action'] = 'Atualizar'
        context['fornecedor'] = self.object
        return context


class FornecedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Fornecedor
    template_name = 'cadastros/fornecedor_confirm_delete.html'
    success_url = reverse_lazy('cadastros:fornecedor_list')
    context_object_name = 'fornecedor'
    pk_url_kwarg = 'pk'
    
    def get_object(self, queryset=None):
        """Override para buscar pelo CodFor"""
        if queryset is None:
            queryset = self.get_queryset()
        
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            try:
                return queryset.get(CodFor=pk)
            except Fornecedor.DoesNotExist:
                from django.http import Http404
                raise Http404(f"Fornecedor com código '{pk}' não encontrado.")
        
        raise AttributeError("FornecedorDeleteView deve ser chamado com um pk.")


# ============= VIEWS PRODUTOS =============

class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'cadastros/produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = Produto.objects.all()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(CodProd__icontains=search) |
                Q(Descricao__icontains=search)
            )
        return queryset.order_by('CodProd')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['total_produtos'] = Produto.objects.count()
        return context


class ProdutoDetailView(LoginRequiredMixin, DetailView):
    model = Produto
    template_name = 'cadastros/produto_detail.html'
    context_object_name = 'produto'
    pk_url_kwarg = 'pk'
    
    def get_object(self, queryset=None):
        """Override para buscar pelo CodProd"""
        if queryset is None:
            queryset = self.get_queryset()
        
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            try:
                return queryset.get(CodProd=pk)
            except Produto.DoesNotExist:
                from django.http import Http404
                raise Http404(f"Produto com código '{pk}' não encontrado.")
        
        raise AttributeError("ProdutoDetailView deve ser chamado com um pk.")


class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'cadastros/produto_form.html'
    success_url = reverse_lazy('cadastros:produto_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Novo Produto'
        context['action'] = 'Criar'
        return context
    
    def form_valid(self, form):
        try:
            codigo = form.cleaned_data['CodProd'].upper().strip()
            if Produto.objects.filter(CodProd=codigo).exists():
                messages.error(self.request, f'Produto com código "{codigo}" já existe!')
                return self.form_invalid(form)
            
            instance = form.save(commit=False)
            instance.CodProd = codigo
            instance.save()
            
            messages.success(self.request, f'Produto "{codigo}" criado com sucesso!')
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f'Erro ao criar produto: {str(e)}')
            return self.form_invalid(form)


class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'cadastros/produto_form.html'
    pk_url_kwarg = 'pk'
    
    def get_object(self, queryset=None):
        """Override para buscar pelo CodProd"""
        if queryset is None:
            queryset = self.get_queryset()
        
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            try:
                return queryset.get(CodProd=pk)
            except Produto.DoesNotExist:
                from django.http import Http404
                raise Http404(f"Produto com código '{pk}' não encontrado.")
        
        raise AttributeError("ProdutoUpdateView deve ser chamado com um pk.")
    
    def get_success_url(self):
        return reverse_lazy('cadastros:produto_detail', kwargs={'pk': self.object.CodProd})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar Produto - {self.object.CodProd}'
        context['action'] = 'Atualizar'
        context['produto'] = self.object
        return context


class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'cadastros/produto_confirm_delete.html'
    success_url = reverse_lazy('cadastros:produto_list')
    context_object_name = 'produto'
    pk_url_kwarg = 'pk'
    
    def get_object(self, queryset=None):
        """Override para buscar pelo CodProd"""
        if queryset is None:
            queryset = self.get_queryset()
        
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            try:
                return queryset.get(CodProd=pk)
            except Produto.DoesNotExist:
                from django.http import Http404
                raise Http404(f"Produto com código '{pk}' não encontrado.")
        
        raise AttributeError("ProdutoDeleteView deve ser chamado com um pk.")