from django import template
from ..models import Client, Project

register = template.Library()    
    
@register.filter
def get_all_clients(self):
    return Client.objects.all()

@register.filter
def get_related_projects(self, client):
    return Project.objects.filter(client_reference = client)