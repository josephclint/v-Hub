from django import forms

from models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video', 'title', 'description', 'categories', 'tags']
        widgets = {
<<<<<<< Updated upstream
            'title': forms.TextInput(attrs={
                'id': 'up_vid_title',
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            'description': forms.Textarea(attrs={
                'id': 'up_vid_des',
                'class': 'form-control',
                'placeholder': 'Description',
                'wrap': 'hard',
                'rows': 3,
            }),
            'categories': forms.SelectMultiple(attrs={
                'id': 'up_vid_cat',
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            'tags': forms.TextInput(attrs={
                'id': 'tags_panel',
                'class': 'form-control',
                'placeholder': 'Tags',
            }),
            'video': forms.FileInput(attrs={
                'accept': 'video/*'
            })
=======
        	'title': forms.TextInput(attrs={
        		'id': 'up_vid_title',
        		'class': 'form-control',
        		'placeholder': 'Title',
        	}),
        	'description': forms.Textarea(attrs={
        		'id': 'up_vid_des',
        		'class': 'form-control',
        		'placeholder': 'Description',
        		'wrap': 'hard',
        		'rows': 3,
        	}),
        	'categories': forms.SelectMultiple(attrs={
        		'id': 'up_vid_cat',
        		'class': 'form-control',
        	}),
        	'tags': forms.TextInput(attrs={
        		'id': 'tags_panel',
        		'class': 'form-control',
        		'placeholder': 'Tags',
        	}),
        	'video': forms.FileInput(attrs={
				'accept': 'video/*'
        	})
>>>>>>> Stashed changes
        }

    def save(self, commit=True):
        self.data['tags'] = self.data['tags'].strip().split(";")
        return super(VideoForm, self).save(commit=commit)
