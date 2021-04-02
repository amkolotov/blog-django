from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .forms import BlogUserCreationForm, BlogUserLoginForm, BlogUserEditForm, BlogUserProfileEditForm


class RegisterCreateView(CreateView):
    """Регистрация нового пользователя"""
    template_name = 'auth_app/register.html'
    form_class = BlogUserCreationForm
    success_url = reverse_lazy('auth_app:login')


class SignInLoginView(LoginView):
    """Вход в учетную запись пользователя"""
    authentication_form = BlogUserLoginForm
    template_name = 'auth_app/login.html'


class SingOutLogoutView(LogoutView):
    """Выход из учетной записи пользователя"""


@transaction.atomic
def edit(request):
    """Редактирование профиля пользователя"""
    if request.method == 'POST':
        edit_form = BlogUserEditForm(request.POST, instance=request.user)
        profile_form = BlogUserProfileEditForm(request.POST, request.FILES, instance=request.user.bloguserprofile)

        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth_app:edit'))

    else:
        edit_form = BlogUserEditForm(instance=request.user)
        profile_form = BlogUserProfileEditForm(instance=request.user.bloguserprofile)

    context = {
        'edit_form': edit_form,
        'profile_form': profile_form
    }
    return render(request, 'auth_app/edit.html', context)



