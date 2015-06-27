from django import forms

from models import Video

class VideoForm(forms.ModelForm):
	video = forms.FileField(widget=forms.FileInput(attrs={'accept': 'video/*'}))

	class Meta:
		model = Video
		exclude = ['owner', 'datetime_added', 'datetime_modified']