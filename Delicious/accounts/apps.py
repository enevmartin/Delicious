from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Delicious.accounts'

    def ready(self):
        import Delicious.accounts.signals