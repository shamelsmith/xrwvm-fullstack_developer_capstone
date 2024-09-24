"""
Django apps for djangoapp project.

"""
from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    """_summary_

    Args:
        models (model.Model): Django Model Object

    Returns:
        object: a Car Make Object
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    create_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.name}'


class CarModel(models.Model):
    """_summary_

    Args:
        models (model.Model): Django Model Object

    Returns:
        object: Car Model Object
    """
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2015,
                               validators=[
                                    MaxValueValidator(2023),
                                    MinValueValidator(2015)
                                ])
    create_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.car_make.name}: {self.name}'
