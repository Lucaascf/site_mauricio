from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Apps URLs
    path('', include('apps.core.urls')),
    path('cadastros/', include('apps.cadastros.urls')),
    # path('comercial/', include('apps.comercial.urls')),
    # path('ocorrencias/', include('apps.ocorrencias.urls')),
    # path('relatorios/', include('apps.relatorios.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin customization
admin.site.site_header = "Gestão Comercial"
admin.site.site_title = "Gestão Comercial"
admin.site.index_title = "Painel Administrativo"