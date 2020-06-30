from django import forms
from .models import Usuario

#Se crea un formulario con todos los atributos del modelo
class FormRegModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre", "email"]
        
    def clean_email(self):
        email = self.cleaned_data
        return email


#Datos que se van a necesitar en dicho formulario
class FormReg(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
