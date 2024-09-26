"""
URL configuration for beef project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('', include('home.urls')),
    path('dashboard/', include('dashboard.urls')),
    
    path('fazenda/', include('fazenda.urls')),
    path('lote/', include('lote.urls')),
    path('movimentacaoLote/', include('movimentacaoLote.urls')),
    path('animal/', include('animal.urls')),
    path('pasto/', include('pasto.urls')),
    path('movimentacao/', include('movimentacao.urls')),
    path('pesagem/', include('pesagem.urls')),
    path('vendido/', include('vendido.urls')),
    path('morto/', include('morto.urls')),
    path('procedimento/', include('procedimento.urls')),
    path('financeiro/', include('financeiro.urls')),
    
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')))
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





