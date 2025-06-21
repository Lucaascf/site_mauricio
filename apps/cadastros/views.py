from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q
from .models import Cliente, Fornecedor, Produto
from .forms import ClienteForm, FornecedorForm, ProdutoForm

# ============ CLIENTE VIEWS ============
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'cadastros/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 25
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(CodCli__icontains=search) |
                Q(RazaoSoc__icontains=search) |
                Q(Cnpj__icontains=search) |
                Q(Cidade__icontains=search)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'cadastros/cliente_detail.html'
    context_object_name = 'cliente'

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cadastros/cliente_form.html'
    success_url = reverse_lazy('cadastros:cliente_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Cliente criado com sucesso!')
        return super().form_valid(form)

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cadastros/cliente_form.html'
    success_url = reverse_lazy('cadastros:cliente_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Cliente atualizado com sucesso!')
        return super().form_valid(form)

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'cadastros/cliente_confirm_delete.html'
    success_url = reverse_lazy('cadastros:cliente_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Cliente removido com sucesso!')
        return super().delete(request, *args, **kwargs)

# ============ FORNECEDOR VIEWS ============
class FornecedorListView(LoginRequiredMixin, ListView):
    model = Fornecedor
    template_name = 'cadastros/fornecedor_list.html'
    context_object_name = 'fornecedores'
    paginate_by = 25
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(CodFor__icontains=search) |
                Q(RazaoSoc__icontains=search) |
                Q(Cnpj__icontains=search) |
                Q(Cidade__icontains=search)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class FornecedorDetailView(LoginRequiredMixin, DetailView):
    model = Fornecedor
    template_name = 'cadastros/fornecedor_detail.html'
    context_object_name = 'fornecedor'

class FornecedorCreateView(LoginRequiredMixin, CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'cadastros/fornecedor_form.html'
    success_url = reverse_lazy('cadastros:fornecedor_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Fornecedor criado com sucesso!')
        return super().form_valid(form)

class FornecedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'cadastros/fornecedor_form.html'
    success_url = reverse_lazy('cadastros:fornecedor_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Fornecedor atualizado com sucesso!')
        return super().form_valid(form)

class FornecedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Fornecedor
    template_name = 'cadastros/fornecedor_confirm_delete.html'
    success_url = reverse_lazy('cadastros:fornecedor_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Fornecedor removido com sucesso!')
        return super().delete(request, *args, **kwargs)

# ============ PRODUTO VIEWS ============
class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'cadastros/produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 25
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(CodProd__icontains=search) |
                Q(Descricao__icontains=search)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class ProdutoDetailView(LoginRequiredMixin, DetailView):
    model = Produto
    template_name = 'cadastros/produto_detail.html'
    context_object_name = 'produto'

class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'cadastros/produto_form.html'
    success_url = reverse_lazy('cadastros:produto_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Produto criado com sucesso!')
        return super().form_valid(form)

class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'cadastros/produto_form.html'
    success_url = reverse_lazy('cadastros:produto_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Produto atualizado com sucesso!')
        return super().form_valid(form)

class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'cadastros/produto_confirm_delete.html'
    success_url = reverse_lazy('cadastros:produto_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Produto removido com sucesso!')
        return super().delete(request, *args, **kwargs)