from django.apps import AppConfig


class ApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app'

    def ready(self):
        import api_app.signals