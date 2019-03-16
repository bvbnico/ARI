"""ARI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.urls import include
from django.views.generic import RedirectView
from servidor import views

urlpatterns = [

    #url(r'^$', views.home, name='home'),
    #path('home/', include('servidor.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    path('home/', include('servidor.urls')),
    #path('login/', include('servidor.urls')),
    path('admin/', admin.site.urls),
    url('login/', views.login, name='login'),
    path('', RedirectView.as_view(url='/home/', permanent=True)), #redirigir la pàgina principal a esta URL
]


# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
