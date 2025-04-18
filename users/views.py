from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse


def CreatedUser(request):
    '''
    Регистрирует юзера используя стандартную форму.
    После направляет на страницу авторизацией.
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LoginPage')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    '''
    Кастомная версия LoginView для перенаправления на главную
    страницу после успешной авторизации.
    '''
    redirect_authenticated_user = True
    template_name = 'registration/login.html'

    def get_success_url(self):
        """Возвращает URL главной страницы после логина."""
        return reverse('HomePage')
