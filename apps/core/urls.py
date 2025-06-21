from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.cadastros.models import Cliente, Fornecedor, Produto

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes_count'] = Cliente.objects.count()
        context['fornecedores_count'] = Fornecedor.objects.count()
        context['produtos_count'] = Produto.objects.count()
        return context

app_name = 'core'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
]