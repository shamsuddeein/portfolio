from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # Import messages framework
from .models import Project, Contact
from .forms import ContactForm  # Import the correct form


def homePage(request):
    # Change [:2] to all() or just remove the slice to get everything
    projects = Project.objects.all() 
    return render(request, 'portfolio/home.html', {'projects': projects})

def resume(request):
    return render(request, 'portfolio/resume.html')


def contact(request):
    if request.method == 'GET':
        form = ContactForm()  # Use the ContactForm
        return render(request, 'portfolio/contacts.html', {'form': form})
    else:
        try:
            form = ContactForm(request.POST)  # Use ContactForm to process data
            if form.is_valid():
                form.save()  # Save the form if valid
                messages.success(request, "Your message has been sent successfully!")  # Success message
                return redirect('contact')  # Redirect to the same page after submission
        except ValueError:
            return render(request, 'portfolio/contacts.html', {'form': form, 'error': 'Invalid input'})


def ListView(request):
    lists = Project.objects.all()

    return render(request, 'portfolio/lists.html', {'lists': lists})

