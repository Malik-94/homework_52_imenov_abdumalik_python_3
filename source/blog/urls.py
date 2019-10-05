"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import IndexView, TaskCreateView, TaskUpdateView ,TaskDeleteView,TaskView, StatusList ,StatusCreateView ,StatusDeleteView, StatusUpdateView, TypeList, TypeCreateView, TypeUpdateView, TypeDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('articles/add/', TaskCreateView.as_view(), name='task_add'),
    path('article/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('article/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('status/', StatusList.as_view(), name='status_list'),
    path('statuses/add/', StatusCreateView.as_view(), name='status_add'),
    path('status/<int:pk>/edit/', StatusUpdateView.as_view(), name='status_update'),
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('type/', TypeList.as_view(), name='type_list'),
    path('types/add/', TypeCreateView.as_view(), name='type_add'),
    path('type/<int:pk>/edit/', TypeUpdateView.as_view(), name='type_update'),
    path('type/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete'),
]
