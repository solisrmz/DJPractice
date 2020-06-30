from django.contrib import admin
#Importar el model
from .models import Usuario
from .forms import FormRegModelForm
#Para poder personalizar el model en la vista del admin
class AdminUsuario(admin.ModelAdmin):
    list_display = ["email", "nombre", "timesstamp"]
    #Se carga el model en el admin
    form = FormRegModelForm
    #cargando campos
    list_display_links= ["email"]
    list_filter = ["timesstamp"]
    list_editable =["nombre"]
    search_fields = ["nombre", "email", "timestamp"]
    #class Meta:
     #   model = Usuario

# Register your models here.
admin.site.register(Usuario, AdminUsuario)