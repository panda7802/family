"""family URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include

from family import settings
from love.views import *

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', t_index),
    # url(r'^static/(?P<path>.*)$', serve, {'document_root', settings.STATIC_ROOT, }),
    url(r'^love/', love_index),
    url(r'^marry/', marry),
    url(r'^loveaction/(.*)$', love_action),
    url(r'^growing_up/', growing_up),
    url(r'^files/', include('filer.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
