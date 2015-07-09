from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.core.urlresolvers import reverse
from django.contrib.auth import views as auth_views 

from django.views import generic

from app import views as app_views
from sitemap import views as sitemap_views
from forms import UserSignupForm

from django.conf import settings
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy


def anonymous_required(function):
    def as_view(request, *args, **kwargs):
        redirect_to = kwargs.get('next', settings.LOGIN_REDIRECT_URL )
        if request.user.is_authenticated():
            return redirect(redirect_to)

        response = function(request, *args, **kwargs)
        return response
    return as_view

        
class IndexView(generic.View):
    def get(self, request):
        if request.user.is_authenticated():
            return app_views.IndexView.as_view()(request)

        return sitemap_views.IndexView.as_view()(request)


class SignupView(generic.View):
    def post(self, request):
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['post_register_user'] = form.cleaned_data
            return HttpResponseRedirect(reverse('accounts:post_register'))
        else:
            return render(request, 'accounts/signup.html', {
                'form': form,
            })

    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('accounts:index'))

        form = UserSignupForm()
        return render(request, 'accounts/signup.html', {
            'form': form,
        })


class PostRegisterView(generic.View):
    def get(self, request):
        flag = request.session.get('post_register_user', False)

        if request.user.is_authenticated() or not flag:
            return HttpResponseRedirect(reverse('accounts:index'))

        del request.session['post_register_user']
        return render(request, 'accounts/post_register.html', {
            'user': flag
        })


class UserProfileView(generic.TemplateView):
    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def get(self, request):
        if request.user.is_authenticated():
            return render(request,'accounts/profile.html',)


class LogOutView(generic.TemplateView):
    template_name = 'accounts/logout.html'


class SettingsView(generic.TemplateView):
    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def get(self, request):
        if request.user.is_authenticated():
            return render(request,'accounts/settings.html',)


class DisableAccountView(generic.TemplateView):
    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def get(self, request):
        if request.user.is_authenticated():
            return render(request,'accounts/account_disabled.html',)