from django.contrib import admin
from .models import Relation, Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):
	"""
	Inline for displaying Profile model within the admin panel.

	Attributes:
		model (Model): The Profile model to be displayed.
	    can_delete (bool): Determines whether the profile can be deleted or not.
	"""
	model = Profile
	can_delete = False


class ExtendedUserAdmin(UserAdmin):
	inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)
admin.site.register(Relation)
