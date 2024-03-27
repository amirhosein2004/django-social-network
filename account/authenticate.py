from django.contrib.auth.models import User

# Custom authentication backend for authenticating users via email.
class EmailBackend:
	def authenticate(self, request, username=None, password=None):
		try:
			user = User.objects.get(email=username)
			# Check if the provided password is correct.
			if user.check_password(password):
				return user
			return None
		except User.DoesNotExist:
			return None

	# Retrieve user object based on user ID.
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None