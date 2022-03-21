from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer


class TicketView(viewsets.ModelViewSet):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

