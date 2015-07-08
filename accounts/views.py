from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.core.urlresolvers import reverse
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import login 

from django.views import generic

from app import views as app_views
from sitemap import views as sitemap_views
from forms import UserSignupForm

from django.conf import settings

# def anonymous_required( view_function, redirect_to = None ):
#     return AnonymousRequired( view_function, redirect_to )
 
# class AnonymousRequired( object ):
#     def __init__( self, view_function, redirect_to ):
#         if redirect_to is None:
#             from django.conf import settings
#             redirect_to = settings.LOGIN_REDIRECT_URL
#         self.view_function = view_function
#         self.redirect_to = redirect_to
 
#     def __call__( self, request, *args, **kwargs ):
#         if request.user is not None and request.user.is_authenticated():
#             return HttpResponseRedirect( self.redirect_to ) 
#         return self.view_function( request, *args, **kwargs )

        
class IndexView(generic.View):
    def get(self, request):
        if request.user.is_authenticated():
            return app_views.IndexView.as_view()(request)

        return sitemap_views.IndexView.as_view()(request)


class LoginView(generic.View):
    def get(self, request, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        return login(request, **kwargs)


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
    template_name = 'accounts/profile.html'


class LogOutView(generic.TemplateView):
    template_name = 'accounts/logout.html'

class SettingsView(generic.TemplateView):
    template_name = 'accounts/settings.html'

class DisableAccountView(generic.TemplateView):
    template_name = 'accounts/account_disabled.html'
    #This only redirects to the page. The user still needs
    #to be logged out when disabling account

class FollowersView(generic.TemplateView):
    template_name = 'app/followers.html'

class FollowingView(generic.TemplateView):
    template_name = 'app/following.html'
