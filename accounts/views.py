from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import get_user_model, authenticate, login, logout
# Create your views here.
from services.generator import Generator
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


def login_view(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('/')

        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request, "accounts/login.html", context)



def register_view(request):
    form = RegisterForm

    if request.method == "POST":
        form = RegisterForm(request.POST or None)

        if form.is_valid():
            new_user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            new_user.set_password(password)

            new_user.is_active = False # eger is_active deyilse daxil olma
            new_user.activation_code = Generator.create_code_for_activate(size=6, model_=User)
            new_user.activation_code_expires_at = timezone.now() + timezone.timedelta(minutes=15)
            new_user.save()

            # send mail part

            # login(request, new_user)
            return redirect("/")
        else:
            print(form.errors)


    context = {
        "form":form
    }

    return render(request, "accounts/register.html", context)



def logout_view(request):
    logout(request)
    return redirect("/")