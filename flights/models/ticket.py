from django.db import models
from django.contrib.auth.models import User
from .flight import Flight

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    booking_status = models.BooleanField(default=False)

    class Meta:
        unique_together = ('flight', 'seat_number')

    def __str__(self):
        return f"{self.flight} - Seat {self.seat_number}"