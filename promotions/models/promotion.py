from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Promotion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.title} - {self.price}'
