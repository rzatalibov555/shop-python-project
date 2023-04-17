#TODO: "https://docs.djangoproject.com/en/4.2/topics/email/#email-backends"  # send mail ucun documentation

from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm
from django.contrib.auth import get_user_model, authenticate, login, logout
# Create your views here.
from services.generator import Generator
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

User = get_user_model()


def login_view(request):

    form = LoginForm()
    next_url = request.GET.get('next', None)



    if request.method == "POST":
        form = LoginForm(request.POST or None)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)

            login(request, user)

            if next_url:
                return redirect(next_url)
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
            send_mail(
                "Activation_code",
                f"Hi, welcome! Your activation code: <b>{new_user.activation_code}</b> \n Good luck!",
                settings.EMAIL_HOST_USER,
                [new_user.email]
            )

            # login(request, new_user)
            return redirect("accounts:activate-account", slug=new_user.slug)
        else:
            print(form.errors)


    context = {
        "form": form
    }

    return render(request, "accounts/register.html", context)



def logout_view(request):
    logout(request)
    return redirect("/")


def activation_account_view(request, slug):
    user = get_object_or_404(User, slug=slug)

    if request.method == "POST":
        code = request.POST.get("code")

        if code == user.activation_code:
            user.is_active = True
            user.activation_code = None
            user.activation_code_expires_at = None
            user.save()

            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Sizin daxil etdiyiniz kod yalnisdir.")

    context = {}
    return render(request, "accounts/activate.html", context)