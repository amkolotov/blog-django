from django.urls import path

from .views import RegisterCreateView, SignInLoginView, SingOutLogoutView
from .views import edit

app_name = 'auth_app'

urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('login/', SignInLoginView.as_view(), name='login'),
    path('logout/', SingOutLogoutView.as_view(), name='logout'),
    path('edit/', edit, name='edit'),
]
