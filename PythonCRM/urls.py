"""PythonCRM URL Configuration

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
from django.urls import path, include

from client_projects.views import *
from client_projects.client_views import *
from client_projects.project_views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', signup, name='Register'),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='Home'),
    path('clients/', ClientsListView.as_view(), name="ClientsList"),
    path('projects/', ProjectsListView.as_view(), name="ProjectsList"),

    path('client/update/', update_client, name="ClientUpdate"),
    path('client/delete/', delete_client, name="ClientDelete"),
    path('client/create/', create_client, name="ClientCreate"),

    path('project/update/', update_project, name="ProjectUpdate"),
    path('project/delete/', delete_project, name="ProjectDelete"),
    path('project/create/', create_project, name="ProjectCreate"),
]
