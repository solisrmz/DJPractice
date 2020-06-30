from django.shortcuts import render
from .forms import FormReg
from .models import Usuario
# Create your views here.
def inicio(request):
    form = FormReg(request.POST or None)
    #Para hacer las validaciones
    if form.is_valid():
        form_data = form.cleaned_data
        mail = form_data.get("email")
        nm = form_data.get("name")

        usuario = Usuario()
        usuario.email = mail
        usuario.nombre = nm
        usuario.save()

    #Contexto    
    context={
        'my_form':form,
    }
    #Retorna un request, una vista y un contexto
    return render(request, "Inicio.html", context)