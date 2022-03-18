from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'worker', 'status', 'category')
    list_filter = ('status', 'category')
