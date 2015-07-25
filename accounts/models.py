from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User)
    # picture = models.ImageField(
    #     upload_to='profile_pictures',
    #     null=True,
    #     blank=True
    # )
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
    birthday = models.DateField(blank=True, null=True)

    def get_verbose_gender(self):
        for gender in self.GENDER_CHOICES:
            if gender[0] == self.gender:
                return gender[1]
        return 'X'  # this should not happen

    def __unicode__(self):
        return self.user.username
