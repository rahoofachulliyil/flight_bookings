from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, TicketViewSet, UserViewSet

router = DefaultRouter()
router.register(r'flights', FlightViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]