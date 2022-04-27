from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from comments.models import Comment

from comments.views import comments_home
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.


class AddUserCreateView(SuccessMessageMixin ,CreateView):
    model = User
    template_name = 'accounts/add_user.html'
    fields = [
        'first_name',
        'last_name',
        'username',
        'email',
        'password',
    ]
    success_url = reverse_lazy('accounts:add_user')
    success_message = _('Conta criada com sucesso. Faça o login')

    def form_valid(self, form):
        f = form.save(commit=False)
        f.set_password(f.password)
        f.save()
        messages.success(self.request, _('Conta criada com sucesso'))
        return redirect(self.success_url)


class UserLogin(LoginView):
    template_name = 'accounts/user_login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, _('Login realizado com sucesso.'))
            return redirect('accounts:dashboard')
        messages.error(request, _('Erro, login não realizado.'))
        return redirect('accounts:user_login')


@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    comments_unread = Comment.objects.filter(read=False, user=request.user).order_by('-id')
    comments_read = Comment.objects.filter(read=True, user=request.user).order_by('-id')
    context = {
        'comments_unread': comments_unread, 
        'comments_read': comments_read,
    }
    return render(request, template_name, context)

def create_profile(request):
    template_name = 'accounts/user_profile.html'
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, _('Perfil salvo com sucesso.'))
            return redirect('accounts:dashboard')
        else:
            print(form.errors)
    else:
        form = ProfileForm()

    context = {
        'form': form
    }
    return render(request, template_name, context )


@login_required
def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')