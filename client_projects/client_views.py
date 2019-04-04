# Views relating to the Client model

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, redirect
import json

from .models import Client

class ClientsListView(LoginRequiredMixin, View):
    template_name = "clientsList.html"

    def get(self, request):
        return render(request, self.template_name, {'clients': Client})

# Updating an existing client
# We get the values from a JSON encoded string
def update_client(request):
    if request.method == 'POST':
        data = request.body
        json_data = json.loads(data)
        obj = Client.objects.get(pk = json_data.get("id"))
        obj.client_name = json_data.get("clientName")
        obj.contact_person = json_data.get("clientContactPerson")
        obj.contact_number = json_data.get("clientContactNumber")
        obj.save()
        return JsonResponse({'result':'ok'})
    else:
        return JsonResponse({'result':'not ok'})

# Deleting an existing client
def delete_client(request):
    if request.method == 'POST':
        data = request.body
        json_data = json.loads(data)
        obj = Client.objects.get(pk = json_data.get("id"))
        obj.delete()
        return JsonResponse({'result':'ok'})
    else:
        return JsonResponse({'result':'not ok'})

# Creating a new client
def create_client(request):
    if request.method == 'POST':
        obj = Client.objects.create()
        return JsonResponse({'result':'ok', 'id':obj.id})
    else:
        return JsonResponse({'result':'not ok'})