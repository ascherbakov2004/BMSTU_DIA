from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Passport, News

@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ('passport_number', 'full_name', 'photo_preview')

    def photo_preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100" height="100" />')
        return "(Нет фото)"

    photo_preview.short_description = "Фото"

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')
    search_fields = ('title',)
    ordering = ('-date_published',)