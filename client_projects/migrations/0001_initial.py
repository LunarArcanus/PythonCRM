# Generated by Django 2.1.7 on 2019-03-30 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50)),
                ('contact_person', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('project_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Complete', 'Complete')], max_length=20)),
                ('client_reference', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client_projects.Client')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='project_reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client_projects.Project'),
        ),
    ]