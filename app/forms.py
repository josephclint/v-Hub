from django.forms import ModelForm

from models import Video

class VideoForm(ModelForm):
	class Meta:
		model = Video
		exclude = ['owner', 'datetime_added', 'datetime_modified']