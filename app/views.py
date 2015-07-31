from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from models import Video, Tag, Category
from forms import VideoForm
from utils import do_the_tags_magic


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view, login_url=reverse_lazy('accounts:login'))


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


class UploadView(LoginRequiredMixin, generic.View):

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
            context = {'video_upload_form': form}
            return render(request, 'app/upload.html', context)

    def get(self, request):
        context = {'video_upload_form': VideoForm()}
        return render(request, 'app/upload.html', context)


class FollowersView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request):
            return render(request, 'app/followers.html',)


class FollowingView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request):
        return render(request, 'app/following.html',)


class TagVideosView(generic.ListView):
    template_name = 'app/video_list.html'
    context_object_name = 'videos'

    def get_queryset(self):
        try:
            tag = Tag.objects.get(tag_text__iexact=self.args[0])
            return tag.video_set.all()
        except Tag.DoesNotExist:
            return []


class CategoryVideosView(generic.ListView):
    template_name = 'app/category_video_list.html'
    context_object_name = 'videos'

    def get_queryset(self):
        arg = self.args[0].replace('-', ' ').replace(' and ', ' & ')
        category = get_object_or_404(Category, category_text__iexact=arg)
        return category.video_set.all()

    def get_context_data(self, **kwargs):
        arg = self.args[0].replace('-', ' ').replace(' and ', ' & ')
        category = get_object_or_404(Category, category_text__iexact=arg)
        context = super(CategoryVideosView, self).get_context_data(**kwargs)
        context['category'] = category
        return context


class AddComment(generic.View):
    def post(self, request):
        pass


class HomeView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request):
        return render(request, 'app/home.html',)
