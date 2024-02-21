from django.db import models

# Create your models here.
class Menu(models.Model):
    Titel = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Inventory = models.IntegerField()

    def  __str__(self):
        return self.Titel 
    
class Booking(models.Model):
    Name = models.CharField(max_length=100)
    No_Of_Guests = models.IntegerField()
    BookingDate = models.DateTimeField()

    def   __str__(self):
        return self.Name
    