# Generated by Django 4.2.1 on 2023-07-02 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("firsrtapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]
