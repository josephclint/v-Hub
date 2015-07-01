from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from app.views import index as user_index
from sitemap.views import index as website_index
from forms import UserSignupForm

def index(request):
    if request.user.is_authenticated():
        return user_index(request)
    
    return website_index(request)


def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('accounts:index'))

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['post_register_user'] = form.cleaned_data
            return HttpResponseRedirect(reverse('accounts:post_register'))
    else:
        form = UserSignupForm()
    
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


def post_register(request):
    flag = request.session.get('post_register_user', False)

    if request.user.is_authenticated() or not flag:
        return HttpResponseRedirect(reverse('accounts:index'))

    del request.session['post_register_user']
    return render(request, 'accounts/post_register.html', {
        'user': flag
    })