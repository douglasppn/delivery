from delivery.ext.db import models, db # noqa
from delivery.ext.auth.admin import UserAdmin
from delivery.ext.admin import admin

def init_app(app):
	"""TODO: inicializar Flask SImple Login + JWT"""

	admin.add_view(UserAdmin(models.User, db.session))