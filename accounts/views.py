from django.conf import settings
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import (
    HttpResponseRedirect, HttpResponseForbidden,
    JsonResponse
)
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import generic

from app import views as app_views
from sitemap import views as sitemap_views
from forms import UserSignupForm, UserEditProfileForm


def anonymous_required(function):
    def as_view(request, *args, **kwargs):
        redirect_to = kwargs.get('next', settings.LOGIN_REDIRECT_URL)
        if request.user.is_authenticated():
            return redirect(redirect_to)

        response = function(request, *args, **kwargs)
        return response
    return as_view


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view, login_url=reverse_lazy('accounts:login'))


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

            # data = form.cleaned_data
            # request.session['post_register_user'] = data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)

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


class UserProfileView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request):
        return render(request, 'accounts/profile.html',)


class ProfileView(generic.DetailView):
    model = User
    template_name = 'accounts/profile.html'


class LogOutView(generic.TemplateView):
    template_name = 'accounts/logout.html'


class SettingsView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request):
        return render(request, 'accounts/settings.html',)


class DisableAccountView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request):
        request.user.delete()
        return render(request, 'accounts/account_disabled.html',)


class EditProfileView(generic.View):

    def get(self, request):
        user = self.request.user
        data = {
            'birthday': user.userprofile.birthday,
            'gender': user.userprofile.gender,
        }
        form = UserEditProfileForm(instance=user, initial=data)
        return render(request, 'accounts/edit_profile.html', {'form': form})

    def post(self, request):
        form = UserEditProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(pk=request.user.pk)
            user.userprofile.birthday = form.cleaned_data['birthday']
            user.userprofile.gender = form.cleaned_data['gender']
            user.userprofile.save()
            return HttpResponseRedirect(reverse('accounts:user_profile'))
        else:
            return render(request, 'accounts/edit_profile.html', {
                'form': form
            })


class ChangePasswordView(LoginRequiredMixin, generic.View):
    def post(self, request):
        if request.is_ajax():
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})
        else:
            return HttpResponseForbidden()

    def get(self, request):
        return JsonResponse({'success': True})
