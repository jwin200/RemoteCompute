from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class ExecutableModel(models.Model):
    choices = [
        ('PYTHON', '.py'),
        ('JAVA', '.java'),
        ('C++', '.cpp'),
    ]
    name = models.CharField(max_length=120,
                            default=None)
    file = models.FileField(upload_to=f'uploads/{None}/',  # Put the name of the dir here
                            default=None,
                            null=True)
    file_type = models.CharField(max_length=120,
                                 choices=choices,
                                 default=None)
    user = models.CharField(max_length=120,
                            default=None)

    def __str__(self):
        return self.name
