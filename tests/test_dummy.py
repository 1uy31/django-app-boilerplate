from django.conf import settings


def test_dummy():
    assert settings.ALLOWED_HOSTS == ["*"]
