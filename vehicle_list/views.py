import re
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Vehicle
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.

# home page
def home(request):
    ctx={}
    ctx['vehicle_list'] = Vehicle.objects.all()
    return render(request, 'index.html',ctx)

def add(request):
    ctx={}
    if request.method =='POST':
        vehicle_Name=request.POST.get('Vehicle_Name',False)  
        speed=request.POST.get('speed',False)  
        average_speed=request.POST.get('average_speed',False)  
        engine_status=request.POST.get('engine_status',False)  
        fuel_level=request.POST.get('fuel_level',False)  
        temperature=request.POST.get('temperature',False)  
        on_off=request.POST.get('on_off',False)  
        slug=request.POST.get('slug',False)  
        if slug:
            Vehicle.objects.filter(slug=slug).update(vehicle_name=vehicle_Name,speed=speed,average_speed=average_speed,engine_status=engine_status,fuel_level=fuel_level,temperature=temperature,on_off=on_off)
        else:
            vehicle=Vehicle(vehicle_name=vehicle_Name,speed=speed,average_speed=average_speed,engine_status=engine_status,fuel_level=fuel_level,temperature=temperature,on_off=on_off)
            vehicle.save()
        ctx['msg']='Data saved'
         
    return render(request, 'add_vehicle.html',ctx)


def update(request):
    ctx={}
    if request.method =='POST':
        value=request.POST.get('value')
        id=request.POST.get('id')
        if value and id:
            check=Vehicle.objects.filter(id=id).update(on_off=value)
            if check == 1:
                ctx["status"]="Success"
            else:
                ctx["status"]="Error"
    return JsonResponse(ctx)


def edit(request, *args, **kwargs):
    ctx={}
    slug=kwargs['slug']
    vehicle=get_object_or_404(Vehicle,slug=slug)
    ctx['vehicle']=vehicle
    return render(request, 'add_vehicle.html',ctx)

def delete(request, *args, **kwargs):
    ctx={}
    slug=kwargs['slug']
    Vehicle.objects.filter(slug=slug).delete()
    ctx['vehicle_list'] = Vehicle.objects.all()
    return render(request, 'index.html',ctx)
    

# product detail page
class VehicleDetail(DetailView):
    model=Vehicle