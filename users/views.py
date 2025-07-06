from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UserRegistrationForm, EmailAuthenticationForm

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')  # Временно, заменим ниже

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()

        # Отправка приветственного письма
        send_mail(
            'Добро пожаловать!',
            'Спасибо за регистрацию на нашем сайте.',
            'from@example.com',  # замени на настоящий sender email
            [user.email],
            fail_silently=False,
        )

        # Логиним пользователя сразу после регистрации
        login(self.request, user)

        # Перенаправляем на главную страницу или на другую нужную
        self.success_url = reverse_lazy('home')
        return response

class CustomLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = 'users/login.html'
