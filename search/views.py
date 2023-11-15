from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Reservation, Vehicle
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime

## searchApp utiliza el index de la aplicacion es la pagina de busqueda
def searchApp(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            lugar = request.POST.get('lugar')
            fecha1 =  datetime.strptime(request.POST.get('fechaRecogida'), "%Y-%m-%d")
            fecha_array1 = [int(fecha1.year), int(fecha1.month), int(fecha1.day)]
            fecha2 = datetime.strptime(request.POST.get('fechaEntrega'), "%Y-%m-%d")
            fecha_array2 = [int(fecha2.year), int(fecha2.month), int(fecha2.day)]
            vehicles = Vehicle.objects.filter(location=lugar)
            print(fecha1)
            print(fecha2)
            return render(request, "cars.html", {
                'array': vehicles,
                'fecha1': str(fecha_array1),
                'fecha2': str(fecha_array2)
                                                 })
             
        elif request.method == "GET":
            return render(request, "index.html")
    else:
        if request.method == "POST":
            lugar = request.POST.get('lugar')
            vehicles = Vehicle.objects.filter(location=lugar)
            return render(request, "cars.html", {'array': vehicles}) 
        elif request.method == "GET":
            return render(request, "index.html")

## Infocar recibe el id del auto y permite mostrar la informacion de un auto
def infocar(request, vehicle_id):
    vehicleQuery = Vehicle.objects.get(id=vehicle_id)
    return render(request, "rentCar.html", {'vehicle':vehicleQuery})
## Infocar recibe el id y las fechas de renta y permite mostrar la informacion de un auto y
def infocarTimes(request, vehicle_id, array1, array2):
    vehicleQuery = Vehicle.objects.get(id=vehicle_id)
    print(f"imagen de retorno: {vehicleQuery.img.url}")
    return render(request, "rentCar.html", {
        'vehicle':vehicleQuery,
        'fecha1': array1,
        'fecha2': array2
        })


def rentCar(request, vehicle_id):
    if request.user.is_authenticated:
        print(f"imagen de retorno: {Vehicle.objects.get(id=vehicle_id).img.url}")
        return render(request, "rent.html", {
            "car": Vehicle.objects.get(id=vehicle_id)
            })
    else:
        return redirect("singin")
     
    
def rentCarTime(request, vehicle_id, array1, array2):
    fecha1_int = [int(item) for item in array1.strip('[]').split(', ')]
    fecha2_int = [int(item) for item in array2.strip('[]').split(', ')]
    price_per_day = Vehicle.objects.get(id=vehicle_id).price
    days = fecha2_int[2] - fecha1_int[2]
    price_total = days * price_per_day
    print(price_total)
    print(days)
    print(fecha1_int)

    if request.user.is_authenticated:
        return render(request, "rent.html", {
            "car": Vehicle.objects.get(id=vehicle_id),
            'array1': array1,
            'array2': array2,
            'price_total': price_total,
            'days': days 
            })
    else:
        return redirect("singin")    
    
def signin(request): 
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
         user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
         if user is None:
            return HttpResponse("Revisa que tus credenciales esten correctas")
         login(request, user)
         return redirect('/')
        except Exception as e:
                return HttpResponse(f"Error al logearse: {str(e)}")



def signup(request):
    if request.method == 'GET':
        return render(request, 'singup.html')
    else:
        try:
            print(request.POST)
            user = User.objects.create_user(
                request.POST["username"],
                password = request.POST["password"], 
                first_name = request.POST["name"], 
                last_name = request.POST["lastname"],
                email = request.POST["email"])
            user.save()
            login(request, user)
            return redirect('/')
        except Exception as e:
                return HttpResponse(f"Error al registrar el usuario: {str(e)}")

def reservar(request):
    if request.method == 'GET':
        return render(request, 'reservar.html')
   


def contacto(request):
    if request.method == 'GET':
        return render(request, 'contacto.html')
   

def editUserInfo (request):
    if request.method =='GET':
        return render (request, 'editUserInfo.html')
    else:
     try:
        if request.method=='POST':
         user_id = request.user.id  
         user = User.objects.get(id=user_id)
        
         new_username = request.POST['newUsername'] # nombre de usuario
         new_firstname= request.POST['newName'] # nombre
         new_Lastname= request.POST['newLastname'] # apellido
         new_email = request.POST['newEmail'] # email
         new_password = request.POST['newPassword'] # contra
        
         user.username = new_username
         user.first_name = new_firstname
         user.last_name = new_Lastname
         user.email = new_email
         user.set_password(new_password)  
         user.save()

         return redirect('/') 
     except Exception as e:
                return HttpResponse(f"Error al editar la informacion: {str(e)}")
        



@login_required
def singout(request):
    logout(request)
    return redirect("/")

@login_required
def rentNow(request, car):
    return HttpResponse("funcione!!!!")


### rento


from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vehicle, Reservation

@login_required
def rentFinal(request, vehicle_id, array1, array2):
    fecha1_int = [int(item) for item in array1.strip('[]').split(', ')]
    fecha2_int = [int(item) for item in array2.strip('[]').split(', ')]
    price_per_day = Vehicle.objects.get(id=vehicle_id).price
    days = fecha2_int[2] - fecha1_int[2]
    price_total = days * price_per_day
    user_id = request.user.id
    formatted_array1 = f"{fecha1_int[0]}-{fecha1_int[1]:02d}-{fecha1_int[2]:02d}"
    formatted_array2 = f"{fecha2_int[0]}-{fecha2_int[1]:02d}-{fecha2_int[2]:02d}"

    reservation = Reservation(
        client_id=user_id,
        vehicle_id=vehicle_id,
        pickup_date=datetime.strptime(formatted_array1, '%Y-%m-%d').date(),
        return_date=datetime.strptime(formatted_array2, '%Y-%m-%d').date(),
        pickup_location=Vehicle.objects.get(id=vehicle_id).location,
    )
    reservation.save()
    context = {
        'vehicle_id': vehicle_id,
        'array1': formatted_array1,
        'array2': formatted_array2,
        'days': days, 
        'price_per_day': price_per_day,
        'price_total': price_total,
        'user': user_id,
    }
    return render(request, 'finalRent.html', context)

    
    


