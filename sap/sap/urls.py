"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from webapp.views import actualizarRegistro,registerView,registroexitoso,loginView,inicio,PaginaAdmin,salida, verUsuario, eliminarCuenta, agregarVehiculo, ServiciosList, paso ,pruebas, VerListService, eliminarRegistro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/',registerView, name="register"),
    path('registroexitoso/',registroexitoso),
    path('inicio/',inicio, name="inicio"),
    path('login/',loginView, name="login"),
    path('settings/',PaginaAdmin, name="confi"),
    path('logout',salida, name="salida"),
    path('verusuarios/', verUsuario, name="listauser"),
    path('eliminar/<int:userID>',eliminarCuenta, name="eliminar"),
    path('elminarRegistro/<int:servicioID>' , eliminarRegistro, name="eliminarVehiculo"),
    path('agregarVehiculo/',agregarVehiculo, name='agregar'),
    path('verservicios/', ServiciosList, name='listaservicios'),
    path('guardo/',paso, name='success'),
    path('pruebas/',pruebas),
    path('verlistavehiculo/', VerListService, name='verVehiculo'),
    path('actualizar/<int:vehiculoID>/', actualizarRegistro, name='actualizar')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
