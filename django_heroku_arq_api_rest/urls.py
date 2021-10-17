"""django_heroku_arq_api_rest URL Configuration

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
from django.contrib import admin
from django.urls import path
from django_heroku_arq_api_rest.ws.client_controller import client
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('', get_schema_view(title="ARQ API REST",description="API EXAMPLE",
    version="1.0.0"), name='home'), 
    path('openapi', get_schema_view(title="ARQ API REST",description="API EXAMPLE",
    version="1.0.0"), name='home'),         
    path('admin/', admin.site.urls),
    path('api/v1/client', client, name="client"),
    
]
