from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from users.models import User
from users.forms import UserRegisterForm, UserForm
from django.core.mail import send_mail
from django.conf import settings
import random
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    #success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()

        code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        self.object.is_active = False
        self.object.verification_code = code
        self.object.save()

        send_mail(
            subject='Поздравляем с регистрацией',
            message=f'Вы зарегистрировались! Ваш код: {code} ',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )

        return super().form_valid(form)

    def get_success_url(self):
        # После регистрации редирект на подтверждение email
        return reverse('users:verify_email', kwargs={'pk': self.object.pk})


class UserUpdateView(UpdateView):

    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):

        return self.request.user


def generate_new_password(request):

    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:home'))


def verify_email(request, pk):

    if request.method == 'POST':
        code_to_check = request.POST.get('verification_code')
        user = User.objects.get(pk=pk)

        if user.verification_code == code_to_check:
            user.is_active = True
            user.save()
            return redirect(reverse('users:login'))

        else:

            raise ValidationError(f'You have used the wrong code!')
    else:

        context = {'page_title': 'Email verification'}
        return render(request, 'users/verify_email.html', context)
