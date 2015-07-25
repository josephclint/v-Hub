from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic

from models import Video
from forms import VideoForm
from utils import do_the_tags_magic


class IndexView(generic.View):
    """
    Displays home page of a user with his uploaded videos
    """
    def get(self, request):
        current_user = User.objects.get(pk=request.user.id)
        videos = current_user.video_set.all()
        return render(request, 'app/videos.html', {
            'videos': videos,
        })


class DetailView(generic.DetailView):
    model = Video
    template_name = 'app/detail.html'


class UploadView(generic.View):
    context = {
        'title': 'Add Video',
        'form_action': reverse_lazy('videos:add'),
        'submit_label': 'Upload',
    }

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def post(self, request):
        tags = do_the_tags_magic(request.POST.get('tags', ''))
        request.POST['tags'] = tags

        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('accounts:index'))
        else:
            self.context['form'] = form
            return render(request, 'app/upload.html', self.context)

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def get(self, request):
        self.context['video_upload_form'] = VideoForm()
        return render(request, 'app/upload.html', self.context)


class FollowersView(generic.TemplateView):
    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def get(self, request):
            return render(request, 'app/followers.html',)


class FollowingView(generic.TemplateView):
    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def get(self, request):
        return render(request, 'app/following.html',)


class VideosView(generic.TemplateView):
    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def get(self, request):
        return render(request, 'app/videos.html',)


class AddComment(generic.View):
    def post(self, request):
        pass


class HomeView(generic.TemplateView):
    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def get(self, request):
        return render(request, 'app/home.html',)
