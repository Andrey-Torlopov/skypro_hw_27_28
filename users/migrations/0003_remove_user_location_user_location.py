# Generated by Django 4.1.7 on 2023-03-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_location"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="location",
        ),
        migrations.AddField(
            model_name="user",
            name="location",
            field=models.ManyToManyField(blank=True, null=True, to="users.location"),
        ),
    ]
