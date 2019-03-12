from django.db import models


class User(models.Model):
    choices = [
        ("User", "User"),
        ("Organization", "Organization")
    ]

    login = models.CharField(max_length=256, unique=True)
    url = models.URLField()
    user_type = models.CharField(max_length=12, choices=choices)

    def __str__(self):
        return "username:{}, {}".format(self.login, self.user_type)


class Repository(models.Model):
    name = models.CharField(max_length=256)
    full_name = models.CharField(max_length=256)
    url = models.URLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "name:{}, owner:{}".format(self.name, self.owner.login)
