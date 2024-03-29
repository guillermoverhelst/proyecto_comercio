"""aplicacion_comercio URL Configuration

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
from django.urls import path
from tienda import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.plt_inicio_sesion, name='inicio_sesion'),
    path('productos/', views.productos, name="productos"),
    path('registro/', views.registro, name='registro'),
    path('agregar_a_carrito/', views.agregar_a_carrito, name='agregar_a_carrito'),
    path('mostrar_carrito/', views.mostrar_carrito, name='mostrar_carrito'),
    path('eliminar_de_carrito/', views.eliminar_de_carrito, name='eliminar_de_carrito'),
    path('pagar_carrito/', views.pagar_carrito, name='pagar_carrito'),
    path('post_trx/', views.post_trx, name='post_trx'),
    path('guardar_carrito/', views.guardar_carrito, name='guardar_carrito'),
    path('auth.js', views.auth_js, name='auth_js'),
]

urlpatterns += staticfiles_urlpatterns()