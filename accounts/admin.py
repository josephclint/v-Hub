from django.contrib import admin
from django.contrib.auth.models import User

from models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Additional Information'


class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Account Information', {'fields': ['username', 'email']}),
        ('Personal Information', {'fields': ['first_name', 'last_name']})
    )

    ('username', 'password')
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
