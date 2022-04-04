from django.apps import AppConfig


class InstaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insta'

    #import signals
    def ready(self):
        import insta.signals