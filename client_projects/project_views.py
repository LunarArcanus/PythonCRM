# Views relating to the Project model

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, redirect
import json

from .models import Client, Project

class ProjectsListView(LoginRequiredMixin, View):
    template_name = "projectsList.html"

    def get(self, request):
        project_statuses = [status for (status, x) in Project._meta.get_field('project_status').choices]
        return render(request, self.template_name, {'projects': Project.objects.all(),
                                                    'clients': Client.objects.all(),
                                                    'project_statuses': project_statuses})

# Updading an existing project
# We get the values from a JSON encoded string
def update_project(request):
    if request.method == 'POST':
        data = request.body
        json_data = json.loads(data)
        obj = Project.objects.get(pk = json_data.get("id"))
        obj.project_name = json_data.get("projectName")
        obj.project_status = json_data.get("projectStatus")
        client_references = Client.objects.filter(client_name = json_data.get("projectClientRef", "No client"))
        if len(client_references) == 0:
            obj.client_reference = None
        else:
            obj.client_reference = client_references[0]
        obj.save()
        return JsonResponse({'result':'ok'})
    else:
        return JsonResponse({'result':'not ok'})

# Deleting an existing project
def delete_project(request):
    if request.method == 'POST':
        data = request.body
        json_data = json.loads(data)
        obj = Project.objects.get(pk = json_data.get("id"))
        obj.delete()
        return JsonResponse({'result':'ok'})
    else:
        return JsonResponse({'result':'not ok'})

# Creating a new project
def create_project(request):
    if request.method == 'POST':
        obj = Project.objects.create()
        return JsonResponse({
            'result':'ok',
            'id':obj.id
        })
    else:
        return JsonResponse({'result':'not ok'})