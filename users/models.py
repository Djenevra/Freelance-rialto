from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal




class User(AbstractUser):
    purchaser = 1
    executor = 2

    user_types = (
        (purchaser, 'purchaser'),
        (executor, 'executor'))

    name = models.CharField(blank = True, max_length = 255)
    user_type = models.PositiveSmallIntegerField(choices = user_types)
    balance = models.DecimalField(decimal_places = 2, max_digits = 7, default = 0)



    def __str__(self):
     return self.username



    def balance_update(self):
        pass
