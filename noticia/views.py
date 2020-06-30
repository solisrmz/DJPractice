from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, FormRegModelForm
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

def contact(request):
    titulo = "Contáctate con nosotros"
    form = ContactForm(request.POST or None)
    if form.is_valid():
     #   for key, value in form.cleaned_data.items():
      #      print(key, value)
        form_email = form.cleaned_data.get("email")
        form_nombre = form.cleaned_data.get("nombre")
        form_mensaje = form.cleaned_data.get("message")
        asunto = "Formulario de contacto"
        email_from = settings.EMAIL_HOST_USER
        email_mensaje = "%s: %s enviado por: %s" %(form_nombre, form_email, form_mensaje)
        send_mail(asunto,
            email_mensaje,
            email_from,
            ['isolisrmz@gmail.com'],
            fail_silently=False
            )  
    context = {
        'titulo':titulo,
        'form':form
    }
    return render(request, "contacto.html", context)    