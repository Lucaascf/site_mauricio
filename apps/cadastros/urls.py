from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    # Cliente URLs - Corrigindo para usar string pk para todos
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/novo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<str:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/<str:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<str:pk>/remover/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    
    # Fornecedor URLs - Corrigindo para usar string pk
    path('fornecedores/', views.FornecedorListView.as_view(), name='fornecedor_list'),
    path('fornecedores/novo/', views.FornecedorCreateView.as_view(), name='fornecedor_create'),
    path('fornecedores/<str:pk>/', views.FornecedorDetailView.as_view(), name='fornecedor_detail'),
    path('fornecedores/<str:pk>/editar/', views.FornecedorUpdateView.as_view(), name='fornecedor_update'),
    path('fornecedores/<str:pk>/remover/', views.FornecedorDeleteView.as_view(), name='fornecedor_delete'),
    
    # Produto URLs - Corrigindo para usar string pk
    path('produtos/', views.ProdutoListView.as_view(), name='produto_list'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<str:pk>/', views.ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/<str:pk>/editar/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<str:pk>/remover/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
]