from django.db import models
from django.utils import timezone
# Create your models here.

class pokevar(models.Model):
    poke_choice=[
        ('Pi','Pikachu'),
        ('Ch','Charmander'),
        ('Sq','Squirtle'),
        ('Bu','Bulbasaur'),
    ]
    name =  models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=100,choices=poke_choice)


    def __str__(self):
        return self.name