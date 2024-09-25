from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Flight
from ..serializers import FlightSerializer
from django.db.models import Q
from datetime import datetime
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get_permissions(self):
    
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        flight = serializer.save()
        flight.initialize_seats()  # Initialize seats for the new flight

    @action(detail=False, methods=['get'])
    def search(self, request):
        departure_city = request.query_params.get('departure_city')
        destination_city = request.query_params.get('destination_city')
        date = request.query_params.get('date')

        queryset = self.get_queryset()

        if departure_city:
            queryset = queryset.filter(departure_city__icontains=departure_city)
        if destination_city:
            queryset = queryset.filter(destination_city__icontains=destination_city)
        if date:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            queryset = queryset.filter(departure_time__date=date_obj)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    