# Generated by Django 4.1 on 2022-08-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Enquery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enq_name', models.CharField(max_length=60)),
                ('enq_email', models.EmailField(max_length=254)),
                ('enq_contact', models.CharField(max_length=15)),
                ('enq_project', models.CharField(max_length=40)),
                ('enq_message', models.TextField()),
            ],
        ),
    ]