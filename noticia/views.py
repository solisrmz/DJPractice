from django.shortcuts import render
from .forms import FormReg, FormRegModelForm
from .models import Usuario
# Create your views here.
def inicio(request):
    titulo = "Hola"
    if request.user.is_authenticated:
        titulo = "Hola %s" %(request.user)
    form = FormRegModelForm(request.POST or None)
    #Para hacer las validaciones
    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.nombre:
            instance.nombre= "Persona1"
        instance.save()

    #Contexto    
    context={
        'saludo':titulo,
        'my_form':form,
    }
    #Retorna un request, una vista y un contexto
    return render(request, "Inicio.html", context)