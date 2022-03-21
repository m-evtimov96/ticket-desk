from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Ticket(models.Model):

    SOFTWARE_PROBLEM = 'software_problem'
    HARDWARE_PROBLEM = 'hardware_problem'
    NETWORK_ISSUE = 'network_issue'
    INFOSEC_ISSUE = 'infosec_issue'

    CATEGORY_CHOICES = {
        (SOFTWARE_PROBLEM, 'Software problem'),
        (HARDWARE_PROBLEM, 'Hardware problem'),
        (NETWORK_ISSUE, 'Networking issue'),
        (INFOSEC_ISSUE, 'Information Security issue'),
    }

    OPEN = 'open'
    IN_PROGRESS = 'in_progress'
    CLOSED = 'closed'

    STATUS_CHOICES = {
        (OPEN, 'Open'),
        (IN_PROGRESS, 'In progress'),
        (CLOSED, 'Closed'),
    }

    title = models.CharField(max_length=70)
    content = models.TextField(max_length=3000)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(UserModel, related_name='tickets', on_delete=models.CASCADE)

    worker = models.ForeignKey(UserModel, related_name='work_tickets', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title