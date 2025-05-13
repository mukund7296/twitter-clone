from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Post

from django.contrib import admin
from .models import Profile

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('avatar',)}),
    )

# Profile Admin (inline with User)
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

# Combine User and Profile
class UserAdminWithProfile(CustomUserAdmin):
    inlines = (ProfileInline,)

# Post Admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('content', 'user__username')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'country', 'occupation')
    search_fields = ('user__username', 'city', 'occupation', 'company')
    list_filter = ('country',)

# Register your models here
admin.site.register(User, UserAdminWithProfile)
admin.site.register(Post, PostAdmin)