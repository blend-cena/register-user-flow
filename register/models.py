from django.contrib.auth.models import AbstractUser, UserManager


class AppUserManager(UserManager):

    def is_trusty_comment(self):
        pass

    def get_admin(self):
        return UserManager.filter(self, is_superuser=True).first()


class AppUser(AbstractUser):
    objects = AppUserManager()
