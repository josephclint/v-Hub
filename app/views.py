from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

from models import Video
from forms import VideoForm

def index(request):
    """
    Displays home page of a user
    """
    current_user = User.objects.get(pk=request.user.id)
    videos = current_user.video_set.all()
    return render(request, 'app/home.html', {
    	'videos': videos,
    })

def detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'app/detail.html', {'video': video})

@login_required
def add(request):
    context = {
        'title': 'Add Video',
        'form_action': reverse('videos:add'),
        'submit_label': 'Upload',
    }

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            return HttpResponseRedirect(reverse('accounts:index'))
        else:
            context['form'] = form
    else:
        context['form'] = VideoForm()
    
    return render(request, 'app/video.html', context)