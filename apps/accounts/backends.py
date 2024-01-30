from typing import Any
from django.http.request import HttpRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.backends import ModelBackend


class CustomBackends(ModelBackend):

    def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        User = get_user_model()
        try:
            user = User.objects.filter(email__exact=username)
        except user.DoesNotExist:
            return

        if user.exists():
            my_user = user.first()
            if my_user.check_password(password):
                return my_user

            return
        return
