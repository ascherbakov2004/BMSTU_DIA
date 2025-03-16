from django.db import models
from django.core.files.storage import default_storage

class Passport(models.Model):
    passport_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    issue_date = models.DateField()
    expiry_date = models.DateField()
    country = models.CharField(max_length=50)
    issuing_authority = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='')  # Загружаем в MinIO

    def __str__(self):
        return f"{self.full_name} ({self.passport_number})"

class BorderCrossingApplication(models.Model):
    passports = models.ManyToManyField(Passport)
    crossing_date = models.DateField()
    flight_number = models.CharField(max_length=20)
    crossing_point = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=50)
    purpose = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заявка {self.id} на {self.crossing_date}"

class News(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_published']
        verbose_name = "Новость"
        verbose_name_plural = "Новости"