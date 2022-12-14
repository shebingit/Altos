# Generated by Django 4.1 on 2022-09-05 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0005_delete_enquery_delete_project_enquery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=40)),
                ('client_discr', models.TextField()),
                ('client_logo', models.ImageField(upload_to='client/')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=40)),
                ('course_discr', models.TextField()),
                ('course_img', models.ImageField(upload_to='course/')),
            ],
        ),
        migrations.CreateModel(
            name='OnProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=40)),
                ('project_discr', models.TextField()),
                ('project_img', models.ImageField(upload_to='project/')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Enquery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enq_name', models.CharField(max_length=60)),
                ('enq_email', models.EmailField(max_length=254)),
                ('enq_contact', models.CharField(max_length=15)),
                ('enq_project', models.CharField(max_length=40)),
                ('enq_message', models.TextField()),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.onprojects')),
            ],
        ),
        migrations.CreateModel(
            name='Enquery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('place', models.CharField(max_length=20)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.courses')),
            ],
        ),
    ]
