from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from config.settings import MESSAGE_TAGS
from .forms import UserRegisterForm, LoginForm, UserUpdateForm, ProfileUpdateForm



class HomeView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ContactView(View):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now proceed to login.')
            return redirect('accounts-login')
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.add_message(self.request, messages.SUCCESS, f'Welcome {username}!')
            return redirect(self.request.GET.get('next', 'pets-home'))
        except:
            messages.add_message(self.request, messages.ERROR,  'Invalid username or password')
            return redirect('accounts-login')


class ProfileView(LoginRequiredMixin, View):
    template_name = 'profile.html'


    def get(self, request, *args, **kwargs):
        context = {
            'u_form': UserUpdateForm(instance=request.user),
            'p_form': ProfileUpdateForm(instance=request.user.profile)
        }
        return render(request, self.template_name, context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.add_message(self.request, messages.SUCCESS, f'Your account has been updated!')
            return redirect('accounts-profile')
        else:
            messages.add_message(self.request, messages.ERROR,  'Problem updating your profile')
            return redirect('accounts-profile')
        

class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('accounts-login')