from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Friendship, FriendshipRequest


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(FriendshipRequest)
class FriendshipRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    pass
