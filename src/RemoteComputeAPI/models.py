from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class FileTest(models.Model):
    name = models.CharField(max_length=120,
                            default=None,
                            null=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/',
                            default=None,
                            null=True)

    def __str__(self):
        return self.name


class ExecutableModel(models.Model):
    choices = [
        ('PY', '.py'),
        ('JV', '.java'),
        ('C++', '.cpp'),
    ]
    name = models.CharField(max_length=120,
                            default=None)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/',
                            default=None,
                            null=True)
    file_type = models.CharField(max_length=120,
                                 choices=choices,
                                 default=None)
    user = models.CharField(max_length=120,
                            default=None)

    def __str__(self):
        return self.name
