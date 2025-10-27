from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

def contact(req):
    contact_form = ContactForm
    if req.method == "POST":
        contact_form = contact_form(data = req.POST)
        if contact_form.is_valid():
            name = req.POST.get('name', '')
            email = req.POST.get('email', '')
            content = req.POST.get('content', '')
            return redirect(reverse('contact') + '?ok')
        
    return render(req, 'contact/contacto.html', {"form": contact_form})