# Generated by Django 4.1.5 on 2023-01-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0004_invite_confirm_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='confirmed',
            field=models.BooleanField(null=True),
        ),
    ]
