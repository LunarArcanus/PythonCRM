# Generated by Django 2.1.7 on 2019-04-09 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_projects', '0003_remove_project_client_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='client_reference',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client_projects.Client'),
        ),
    ]
