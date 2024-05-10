# Generated by Django 5.0.4 on 2024-04-26 17:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0003_pushnotificationsubscription"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Workout",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                (
                    "equipment",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="workouts",
                        to="members.equipment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workouts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]