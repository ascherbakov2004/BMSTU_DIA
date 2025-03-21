# Generated by Django 5.1.7 on 2025-03-16 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("passports", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BorderCrossingApplication",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("passports", models.ManyToManyField(to="passports.passport")),
            ],
        ),
        migrations.DeleteModel(
            name="BorderCrossing",
        ),
    ]
