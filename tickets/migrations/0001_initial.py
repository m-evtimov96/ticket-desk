# Generated by Django 4.0.3 on 2022-03-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('content', models.TextField(max_length=3000)),
                ('category', models.CharField(choices=[('infosec_issue', 'Information Security issue'), ('network_issue', 'Networking issue'), ('software_problem', 'Software problem'), ('hardware_problem', 'Hardware problem')], max_length=20)),
                ('status', models.CharField(choices=[('closed', 'Closed'), ('in_progress', 'In progress'), ('open', 'Open')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
