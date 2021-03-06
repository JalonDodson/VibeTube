from django.contrib import admin
from vibe_user.models import Viber
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# Register your models here.

class ViberAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = Viber
    list_display = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'bio', 'website', 'display_name', 'verified', 'profile_photo']
    fieldsets = [
        (None, {'fields': ('username',  'password', 'email', 'first_name', 'last_name', 'bio', 'website', 'display_name', 'verified', 'profile_photo')})
    ]

admin.site.register(Viber, ViberAdmin)