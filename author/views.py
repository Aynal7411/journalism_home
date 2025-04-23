from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AuthorRegistrationForm  # Import the form
# Create your views here.
def starting_page(request):
    
    return render(request, 'starting_page.html')

def author_register(request):
        form = AuthorRegistrationForm()
        if request.method == 'POST':
           form = AuthorRegistrationForm(request.POST)
           if form.is_valid():
                form.save()
                return redirect('starting_page')
                 # Correct the spelling
        else:
            form = AuthorRegistrationForm()
       
        return render(request, 'author_register.html' , {'form': form})