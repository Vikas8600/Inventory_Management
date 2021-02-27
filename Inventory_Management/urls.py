"""Inventory_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Inventory_Management import settings
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # login logout
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('dashboard/', views.dashoard, name='dashboard'),
    # location
    path('location/', views.location, name='location'),
    path('savelacation/', views.savelacation, name='save_lacation'),
    path('editlacation/', views.editlacation, name='edit'),
    path('deletelacation/', views.deletelacation, name='delete'),
    # product
    path('products/', views.products, name='products'),
    path('save_product/', views.saveproduct, name="save_product"),
    path('deleteproduct/', views.deleteproduct, name='deleteproduct'),
    path('editProduct/',views.editProduct,name="editProduct"),

    # product movement
    path('productmovement/',views.productmovement,name='productmovement'),
    path('productmovementsave/',views.productmovementsave,name='productmovementsave'),
    path('deletemovement/',views.deletemovement,name='deletemovement'),
    path('editmovement/',views.editmovement,name='editmovement'),

    # report
    path('report/',views.report,name='report')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
