from django.shortcuts import render
from .forms import ContactForm

def contact(req):
    contact_form = ContactForm
    return render(req, 'contact/contacto.html', {"form": contact_form})