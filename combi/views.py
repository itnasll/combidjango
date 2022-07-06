from django.shortcuts import render
from time import ctime
from .forms import Consulta_frm
from django.shortcuts import redirect
from .models import Reserva
from django.db.models import Q #
# Create your views here.

def current_datetime(request):
    ahora = ctime()
    return render(request,'combi/hora.html',{"ahora": ahora})



def home(request):
    return render(request, 'combi/home.html',{})

def reserva(request):
    if request.method == "POST":
        form = Consulta_frm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_reserva')
        
    else:
        form = Consulta_frm()
    
    return render(request, 'combi/reserva.html',{'form':form})

def listado(request):
    reservas = Reserva.objects.all()
    return render(request, 'combi/listado.html',{'reservas': reservas})
    
def ayuda(request):
    return render(request, 'combi/ayuda.html',{})

def buscar(request):
    if request.method == "GET":

        query = request.GET.get('q')

        if not query:
            results = ""
        else:
            results = Reserva.objects.filter(Q(nombre__icontains=query)
                                             | Q(telefono__icontains=query) 
                                             | Q(fecha__icontains=query) 
                                             | Q(subeEn__nombre__icontains=query) 
                                             | Q(bajaEn__nombre__icontains=query) )
  

    return render(request, 'combi/buscar.html',{'resultados':results, 'busca':query})