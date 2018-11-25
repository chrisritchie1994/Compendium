"""Compendium URL Configuration

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
from compendium_app.views import JournalCreate, JournalDelete, JournalView, IdeaView, DecisionView, AphorismView, PrincipleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('journal/create/', JournalCreate.as_view(), name='journal_create'),
    path('', JournalCreate.as_view(), name='journal_create'),
    path('journal/<int:pk>/delete/', JournalDelete.as_view(), name='journal_delete'),
    path('journals/', JournalView.as_view(), name='journals'),
    path('ideas/', IdeaView.as_view(), name='ideas'),
    path('decisions/', DecisionView.as_view(), name='decisions'),
    path('aphorisms/', AphorismView.as_view(), name='ideas'),
    path('principles/', PrincipleView.as_view(), name='ideas'),
]
