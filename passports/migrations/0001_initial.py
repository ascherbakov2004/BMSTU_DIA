# Generated by Django 5.1.7 on 2025-03-15 22:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Passport",
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
                ("passport_number", models.CharField(max_length=20, unique=True)),
                ("full_name", models.CharField(max_length=100)),
                ("birth_date", models.DateField()),
                ("issue_date", models.DateField()),
                ("expiry_date", models.DateField()),
                ("country", models.CharField(max_length=50)),
                ("issuing_authority", models.CharField(max_length=100)),
                ("photo", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="BorderCrossing",
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
                ("crossing_date", models.DateField()),
                ("flight_number", models.CharField(max_length=20)),
                ("crossing_point", models.CharField(max_length=100)),
                ("destination_country", models.CharField(max_length=50)),
                ("purpose", models.CharField(max_length=200)),
                (
                    "passport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="passports.passport",
                    ),
                ),
            ],
        ),
    ]
