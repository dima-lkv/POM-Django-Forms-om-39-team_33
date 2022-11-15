from django.db import models
from django.db.models.base import Model
from .models import CustomUser
import bcrypt
from django.contrib.auth.backends import BaseBackend


class CustomAuthentication(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        print('authenticate')
        if email is not None and password is not None:
            user = CustomUser.objects.get(email=email)
            hashed_password = user.password
            print(hashed_password, password)
            is_check = bcrypt.checkpw(password.encode('utf8'), hashed_password.encode('utf8'))
            if is_check == True:
                return user
            else:
                return None
        else:
            return None

    def get_user(self, user_id):
        user = CustomUser.objects.get(id=user_id)
        if user is not None:
            return user
        else:
            return None