# tareas/forms.py
from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_limite', 'categoria']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
        }
