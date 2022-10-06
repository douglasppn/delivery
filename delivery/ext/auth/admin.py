from flask_admin.contrib.sqla import ModelView

# def format_user(self, request, user, *args):
# 	return user.email.split("@")[0]

class UserAdmin(ModelView):
	"""Interface admin de user"""

	column_formatters = {
		"email": lambda s, r, u, *a: u.email.split("@")[0]
	}

	column_searchable_list = ["email"]

	column_list = ["email", "admin "]