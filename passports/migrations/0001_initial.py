# Generated by Django 5.1.7 on 2025-04-03 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                ("is_deleted", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=255)),
                ("link", models.URLField()),
                ("date_published", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
                "ordering": ["-date_published"],
            },
        ),
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
            name="ApplicationPassport",
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
                (
                    "application",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="passports.bordercrossingapplication",
                    ),
                ),
                (
                    "passport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="passports.passport",
                    ),
                ),
            ],
            options={
                "unique_together": {("application", "passport")},
            },
        ),
        migrations.AddField(
            model_name="bordercrossingapplication",
            name="passports",
            field=models.ManyToManyField(
                through="passports.ApplicationPassport", to="passports.passport"
            ),
        ),
    ]
