from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..models import Flight,Ticket
from ..serializers import  TicketSerializer




    
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def available_seats(self, request):
        flight_id = request.query_params.get('flight_id')
        if not flight_id:
            return Response({"error": "Flight ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            flight = Flight.objects.get(id=flight_id)
            print(f"fff{flight}")
        except Flight.DoesNotExist:
            return Response({"error": "Flight not found"}, status=status.HTTP_404_NOT_FOUND)

        tickets = Ticket.objects.filter(flight=flight)
        
        seat_status = [
            {
                "seat_number": ticket.seat_number,
                "is_booked": ticket.booking_status,
                "user": ticket.user.username if ticket.user else None
            }
            for ticket in tickets
        ]

        return Response(seat_status)
    def create(self, request, *args, **kwargs):
        flight_id = request.data.get('flight')
        seat_number = request.data.get('seat_number')

        # Try to get an existing ticket
        ticket = Ticket.objects.filter(flight_id=flight_id, seat_number=seat_number).first()

        if ticket:
            if ticket.booking_status:
                return Response({'detail': 'This seat is already booked.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Update the existing ticket
                serializer = self.get_serializer(ticket, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save(user=request.user, booking_status=True)
        else:
            # Create a new ticket
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user, booking_status=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    @action(detail=False, methods=['get'])
    def my_bookings(self, request):
        tickets = Ticket.objects.filter(user=request.user)
        serializer = self.get_serializer(tickets, many=True)
        return Response(serializer.data)