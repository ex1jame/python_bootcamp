from django.db import models

class Catalog(models.Model):
    name = models.TextField(unique=True)
    
    def __str__(self):
        return self.name