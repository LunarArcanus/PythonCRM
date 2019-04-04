from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate

from .forms import SignUpForm

class HomeView(TemplateView):
    template_name = "index.html"

class RegisterView(TemplateView):
    template_name = "register.html"


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password = raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})