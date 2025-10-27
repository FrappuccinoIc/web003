from django import forms

class ContactForm(forms.Form):
        name = forms.CharField(label = "Nombre", required = True)
        email = forms.EmailField(label = "Correo", required = True)
        content = forms.CharField(label = "Mensaje", required = True, widget = forms.Textarea()) # Textarea nos deja hacer nuestro campo char en multiples lineas
