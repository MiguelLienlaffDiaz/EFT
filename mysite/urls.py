"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
    path('', include('tienda.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Agregar Font Awesome
urlpatterns += [
    path('static/fontawesome/css/all.min.css', lambda r: HttpResponse(open('static/fontawesome/css/all.min.css').read(), content_type='text/css')),
    path('static/fontawesome/js/all.min.js', lambda r: HttpResponse(open('static/fontawesome/js/all.min.js').read(), content_type='application/javascript')),
]
