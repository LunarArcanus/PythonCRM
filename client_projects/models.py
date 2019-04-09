# The models representing the entities involved in the relationship

from django.db import models

class Client(models.Model):
    # project_reference = models.OneToOneField("Project",
    # null = True,
    # blank = True, 
    # on_delete = models.SET_NULL)
    client_name = models.CharField(max_length = 50)
    contact_person = models.CharField(max_length = 50)
    contact_number = models.CharField(max_length = 15)

    def __str__(self):
        return self.client_name

class Project(models.Model):
    client_reference = models.ForeignKey(Client, 
        null = True,
        blank = True,
        on_delete = models.SET_NULL)
    project_name = models.CharField(max_length = 50)
    project_status = models.CharField(max_length = 20, choices = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("Complete", "Complete")
    ))

    def __str__(self):
        return self.project_name