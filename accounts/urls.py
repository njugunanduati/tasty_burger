from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, LoginView, ProfileView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='accounts-register'),
    path('login/', LoginView.as_view(), name='accounts-login'),
    path('profile/', ProfileView.as_view(), name='accounts-profile'),
    path('logout/', LogoutView.as_view(), name='accounts-logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
]