from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from .models import BlogUser, BlogUserProfile


class BlogUserCreationForm(UserCreationForm):
    """Форма регистрации нового пользователя"""
    class Meta:
        model = BlogUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class BlogUserLoginForm(AuthenticationForm):
    """Форма входа в учетную запись пользователя"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class BlogUserEditForm(UserChangeForm):
    """Форма редактирования учетной записи пользователя"""
    class Meta:
        model = BlogUser
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()


class BlogUserProfileEditForm(UserChangeForm):
    """"Форма редактирования профиля пользователя"""
    class Meta:
        model = BlogUserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()


