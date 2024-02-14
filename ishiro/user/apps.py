from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    label = "ishiro_user"
    name = 'ishiro.user'
