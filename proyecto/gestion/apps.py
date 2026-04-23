from django.apps import AppConfig


class GestionConfig(AppConfig):
    name = 'gestion'

    def ready(self):
        if not __import__('os').getenv('VERCEL'):
            return

        from django.contrib.auth import get_user_model
        from django.contrib.auth.models import update_last_login
        from django.contrib.auth.signals import user_logged_in

        user_logged_in.disconnect(update_last_login, sender=get_user_model())
