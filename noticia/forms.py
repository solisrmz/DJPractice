from django import forms
from .models import Usuario

#Se crea un formulario con todos los atributos del modelo
class FormRegModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        #Para validar estructura del email
        email_base, proveeder = email.split("@")
        dominio, extension = proveeder.split(".")
        if not extension == "com":
            raise forms.ValidationError("Por favor ingresa una extension .com en tu email")
        return email
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        return nombre


#Datos que se van a necesitar en dicho formulario
class FormReg(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
