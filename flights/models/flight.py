from django.db import models



class Flight(models.Model):
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.airline} - {self.flight_number}"
    
    def initialize_seats(self, total_seats=100):
        from .ticket import Ticket
        for seat_number in range(1, total_seats + 1):
            Ticket.objects.create(flight=self, seat_number=str(seat_number))
