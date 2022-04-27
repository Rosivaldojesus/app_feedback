
from django.shortcuts import get_object_or_404, redirect, render
from .forms import SearchForm, CommentForm
from accounts.models import Profile
from comments.models import Comment
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.core.mail import BadHeaderError

# Create your views here.

def comments_home(request):
    template_name = 'comments/comments_home.html'
    template_name_results = 'comments/user_search_results.html'
    context = {}
    form = SearchForm()
    query = request.GET.get('query')
    if query:
        profiles = Profile.objects.search(query)
        if profiles:
            context['profiles'] = profiles
        else:
            messages.warning(request, _('Nenhum perfil foi encontrado.'))
        return render(request, template_name_results, context)
    context['form'] = form
    return render(request, template_name, context)


def get_user_profile_or_add_comment(request, username):
    template_name ='comments/get_user_profile_or_add_comment.html'
    context = {}

    user_profile = get_object_or_404(Profile, user__username=username)
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user_profile.user
            f.save()


            #template_email = 'comments/email.txt'
            #try:
            #    form.send_email(form, [user_profile.user.email], template_email)
            #except BadHeaderError:
            #    pass


            messages.success(request, _('Feedback enviado com sucesso.'))
            return redirect('comments:comments_home')
    form = CommentForm()
    context['form'] = form
    context['user_profile'] = user_profile
    return render(request, template_name, context)


def comments_details(request, id_comment):
    comment = get_object_or_404(Comment, pk=id_comment)
    template_name = 'comments/comments_details.html'
    context = {}
    if comment.user == request.user:
        comment.read = True
        comment.save()
        context['comment'] = comment
    else:
        context['message'] = _('Você não possui essa permisão')
    return render(request, template_name, context)

def mark_unread(request, id_comment):
    comment = get_object_or_404(Comment, pk=id_comment)
    if comment.user == request.user:
        comment.read = False
        comment.save()
    else:
        messages.warning(request, _('Não possível executar está função.'))
    
    return redirect('accounts:dashboard')


def comment_delete(request, id_comment):
    comment = get_object_or_404(Comment, pk=id_comment)
    if comment.user == request.user:
        comment.delete()
        messages.success(request, _('Excluído com sucesso'))
    else:
        messages.error(request, _('Não foi possível excluir.'))
    return redirect('accounts:dashboard')