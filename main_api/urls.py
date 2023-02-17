"""main_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(openapi.Info(title='пользуйтесь на здоровье', description='инь и янь', default_version='v1'), public=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docks/', schema_view.with_ui('swagger')),
    path('', include('account.urls')),
    path('', include('game.urls')),
    path('', include('resume.urls')),
    path('', include('news.urls')),
    path('', include('vacancy.urls')),
    # path('', include('company.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)