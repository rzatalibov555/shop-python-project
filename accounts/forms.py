from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

#TODO: Userin fieldleri: 1) Username, 2) mail, 3) first_name, 4) last_name, 5) password
class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput, required=True) # password inputunun type-ni password eledik.

    class Meta:
        model = User
        fields = ("username", "password")


    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = authenticate(username=username, password=password) # check user in db

        if not user:
            raise forms.ValidationError("Username or password invalid")

        if not user.is_active:
            raise forms.ValidationError("Your account is not active")

        return self.cleaned_data
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
            self.fields[field].required = True # ce ya inputun oz icinde daxil edirik required=True kifayet edir.



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password", "password_confirm")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
            self.fields[field].required = True  # ce ya inputun oz icinde daxil edirik required=True kifayet edir.

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username already exists")

        if len(password) < 6:
            raise forms.ValidationError("Minimum lenght is 6")

        if password != password_confirm:
            raise forms.ValidationError("Passwords dont match")

        return self.cleaned_data