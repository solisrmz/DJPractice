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
    #Retorna un request, una vista y el contexto
    return render(request, "base.html", context)

#Vista para el formulario de contacto
def contact(request):
    titulo = "Contáctate con nosotros"
    #se carga el form
    form = ContactForm(request.POST or None)
    #validación del formulario
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_nombre = form.cleaned_data.get("nombre")
        form_mensaje = form.cleaned_data.get("message")
        #Para enviar un correo con los datos de contacto
        asunto = "Formulario de contacto"
        email_from = settings.EMAIL_HOST_USER
        email_mensaje = "%s: %s enviado por: %s" %(form_nombre, form_email, form_mensaje)
        #se envía el mensaje
        send_mail(asunto,
            email_mensaje,
            email_from,
            ['isolisrmz@gmail.com'],
            fail_silently=False
            )  
    #Contexto que será cargado en la vista, titulo de la página y formulario        
    context = {
        'titulo':titulo,
        'form':form
    }
    #se retorna la vista
    return render(request, "contacto.html", context)    

         #   for key, value in form.cleaned_data.items():
      #      print(key, value)