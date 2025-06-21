from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    # Cliente URLs
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/novo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/remover/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    
    # Fornecedor URLs
    path('fornecedores/', views.FornecedorListView.as_view(), name='fornecedor_list'),
    path('fornecedores/<int:pk>/', views.FornecedorDetailView.as_view(), name='fornecedor_detail'),
    path('fornecedores/novo/', views.FornecedorCreateView.as_view(), name='fornecedor_create'),
    path('fornecedores/<int:pk>/editar/', views.FornecedorUpdateView.as_view(), name='fornecedor_update'),
    path('fornecedores/<int:pk>/remover/', views.FornecedorDeleteView.as_view(), name='fornecedor_delete'),
    
    # Produto URLs
    path('produtos/', views.ProdutoListView.as_view(), name='produto_list'),
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/editar/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/remover/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
]