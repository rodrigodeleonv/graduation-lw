# Generated by Django 4.1.5 on 2023-01-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('num_invitations', models.SmallIntegerField(default=1)),
                ('confirmed', models.BooleanField(default=False)),
                ('total_confirmed', models.SmallIntegerField(default=0)),
                ('total_requests', models.IntegerField(default=0)),
            ],
        ),
    ]
