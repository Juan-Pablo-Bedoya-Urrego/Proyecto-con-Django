from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from .forms import formRegistro, formLogin, ServicioForm
from productos.models import Register, Servicios

# Create your views here.
def registerView(request):
    if request.method == 'POST':
        form = formRegistro(request.POST)
        if form.is_valid():
            registroEmail = form.cleaned_data['email']
            registroName = form.cleaned_data['name']
            registroLastname = form.cleaned_data['lastname']
            registroUsername = form.cleaned_data['username']
            registroPassword = form.cleaned_data['password']
            nuevoRegistro = Register(email=registroEmail, name=registroName, lastname=registroLastname,
                                      username=registroUsername, password=registroPassword)
            nuevoRegistro.save()
            user = User.objects.create_user(
                username=registroUsername,
                password=registroPassword,
                email=registroEmail,
                first_name=registroName,
                last_name=registroLastname
            )
            user.save()
            return redirect('login')
    else:
        form = formRegistro()
    return render(request, 'Registro.html', {'form': form})

@staff_member_required
def verUsuario(request):
    query = request.GET.get('search')
    if query:
        users = Register.objects.filter(username=query)
    else:
        users = Register.objects.all()
    return render(request,'Listausers.html',{'users':users})

def eliminarCuenta(request, userID):
    try:
        userDB = get_object_or_404(Register, id=userID)
        userDB.delete()
    except Register.DoesNotExist:
        pass  # No se hace nada si el usuario no existe en la tabla Register

    userDJ = get_object_or_404(User, id=userID)
    userDJ.delete()

    return redirect('listauser')

def eliminarRegistro(request, servicioID):
    servicio = get_object_or_404(Servicios, id=servicioID)
    servicio.delete()

    return redirect('verVehiculo')

def registroexitoso(request):
    return render(request,'registroExitoso.html')

def inicio(request):
    servicios = Servicios.objects.all()
    return render(request,'index.html',{'servicios': servicios})

def loginView(request):
    if request.method == 'POST':
        form = formLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username= username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/inicio')
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = formLogin()
    return render(request,'Login.html', {'form':form})

@staff_member_required
def PaginaAdmin(request):
    return render(request,"paginaAdmin.html")

def salida(request):
    logout(request)
    return redirect('/login')

@staff_member_required
def agregarVehiculo(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            nombreProducto = form.cleaned_data['nombreProducto']
            descripcionProducto = form.cleaned_data['descripcionProducto']
            precioProducto = form.cleaned_data['precioProducto']
            imagenProducto = form.cleaned_data['imagenProducto']

            servis = Servicios(
                nombreProducto=nombreProducto,
                descripcionProducto=descripcionProducto,
                precioProducto=precioProducto,
                imagenProducto=imagenProducto
            )
            servis.save()
            return redirect('verVehiculo')
    else:
        form = ServicioForm()
    return render(request,'AggVehiculo.html',{'form':form})

@staff_member_required
def actualizarRegistro(request, vehiculoID):
    registro = get_object_or_404(Servicios, id = vehiculoID)
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            registro.nombreProducto = form.cleaned_data['nombreProducto']
            registro.descripcionProducto = form.cleaned_data['descripcionProducto']
            registro.precioProducto = form.cleaned_data['precioProducto']
            if 'imagenProducto' in request.FILES:
                registro.imagenProducto = request.FILES['imagenProducto']
            registro.save()
            return redirect('verVehiculo')
    else:
        initial_data = {
            'nombreProducto': registro.nombreProducto,
            'descripcionProducto': registro.descripcionProducto,
            'precioProducto': registro.precioProducto,
        }
        form = ServicioForm(initial=initial_data)
    return render(request, 'ActualizarVehiculo.html', {'form': form})

@staff_member_required
def ServiciosList(request):
    servicios = Servicios.objects.all()
    return render(request,'verServicios.html',{'servicios': servicios})

@staff_member_required
def VerListService(request):
    query = request.GET.get('search')
    if query:
        servicios = Servicios.objects.filter(nombreProducto = query)
    else:
        servicios = Servicios.objects.all()
    return render(request,'tableService.html',{'servicios': servicios})


def paso(request):
    return HttpResponse('si guardo mi amor')

def pruebas(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            nombreProducto = form.cleaned_data['nombreProducto']
            descripcionProducto = form.cleaned_data['descripcionProducto']
            precioProducto = form.cleaned_data['precioProducto']
            imagenProducto = form.cleaned_data['imagenProducto']

            servis = Servicios(
                nombreProducto=nombreProducto,
                descripcionProducto=descripcionProducto,
                precioProducto=precioProducto,
                imagenProducto=imagenProducto
            )
            servis.save()
            return redirect('success')
    else:
        form = ServicioForm()
    return render(request,'pruebas.html',{'form':form})
