"""healthcare URL Configuration

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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from staff import views
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('test2/', views.test, name='test2'),
    path('creator/', views.creator, name='creator'),
    path('contact/', views.contact, name='contact'),
    path('lab/', views.lab, name='lab'),
    path('pharma/', views.pharma, name='pharma'),
    path('spec/', views.spec, name='spec'),
    
    
    path('staffs/', include('staff.urls')),
    path('patients/', include('patients.urls')), 
       
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
