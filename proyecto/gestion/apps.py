from django.apps import AppConfig


class GestionConfig(AppConfig):
    name = 'gestion'

    def ready(self):
        if not __import__('os').getenv('VERCEL'):
            return

        from django.contrib.auth.signals import user_logged_in

        user_logged_in.disconnect(dispatch_uid='update_last_login')
