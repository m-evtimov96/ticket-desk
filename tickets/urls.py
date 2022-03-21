from django.urls import path, include
from rest_framework import routers
from .views import TicketView


router = routers.DefaultRouter()
router.register('tickets', TicketView)

urlpatterns = [
    path('', include(router.urls)),
]