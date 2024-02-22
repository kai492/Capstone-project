from django.db import models

# Create your models here.
class Menu(models.Model):
    Title = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Inventory = models.IntegerField()

    def  __str__(self):
        return f"{self.Title} : {self.Price}"
    
class Booking(models.Model):
    Name = models.CharField(max_length=100)
    No_Of_Guests = models.IntegerField()
    BookingDate = models.DateTimeField()

    def   __str__(self):
        return self.Name
    