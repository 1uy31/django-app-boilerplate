from django.apps import AppConfig


class MainBackendConfig(AppConfig):
    """
    AppConfig for core.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
