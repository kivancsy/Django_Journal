from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('journal:home')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)
