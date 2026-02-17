# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Vacancy, InternshipPeriod, VacancyInternshipPeriod, Application, News

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'vacancy_title', 'status_badge', 'submitted_at_short', 'city']
    list_filter = ['status', 'application_type', 'submitted_at', 'city']
    search_fields = ['first_name', 'last_name', 'email', 'vacancy__title']
    readonly_fields = ['submitted_at', 'created_at']
    list_per_page = 50
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('vacancy', 'application_type', 'internship_period', 'status')
        }),
        ('Персональные данные', {
            'fields': (('first_name', 'last_name', 'middle_name'), 'email', 'phone', 'city')
        }),
        ('Образование', {
            'fields': ('education_institution', 'faculty', 'course'),
            'classes': ('collapse',)
        }),
        ('Профессиональная информация', {
            'fields': ('experience_description', 'motivation', 'resume_url'),
            'classes': ('collapse',)
        }),
        ('Даты', {
            'fields': ('submitted_at', 'reviewed_at', 'created_at'),
            'classes': ('collapse',)
        }),
    )

    def full_name(self, obj):
        return f"{obj.last_name} {obj.first_name}"
    full_name.short_description = 'ФИО'

    def vacancy_title(self, obj):
        return obj.vacancy.title
    vacancy_title.short_description = 'Вакансия'

    def submitted_at_short(self, obj):
        return obj.submitted_at.strftime("%d.%m.%Y %H:%M")
    submitted_at_short.short_description = 'Подана'

    def status_badge(self, obj):
        colors = {
            'NW': 'gray',
            'RV': 'blue', 
            'AC': 'green',
            'RJ': 'red'
        }
        return format_html(
            '<span style="background: {}; color: white; padding: 2px 8px; border-radius: 10px; font-size: 12px;">{}</span>',
            colors.get(obj.status, 'gray'),
            obj.get_status_display()
        )
    status_badge.short_description = 'Статус'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('vacancy', 'internship_period')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_status', 'published_at_short', 'created_at_short']
    list_filter = ['is_published', 'published_at']
    search_fields = ['title', 'content', 'preview']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 30
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'preview', 'content', 'image_url')
        }),
        ('Публикация', {
            'fields': ('is_published', 'published_at')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def published_status(self, obj):
        color = 'green' if obj.is_published else 'red'
        text = 'Опубликовано' if obj.is_published else 'Черновик'
        return format_html(
            '<span style="color: {};">●</span> {}',
            color, text
        )
    published_status.short_description = 'Статус'

    def published_at_short(self, obj):
        return obj.published_at.strftime("%d.%m.%Y") if obj.published_at else '-'
    published_at_short.short_description = 'Дата публикации'

    def created_at_short(self, obj):
        return obj.created_at.strftime("%d.%m.%Y")
    created_at_short.short_description = 'Создана'

# Старые модели оставляем как есть
@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'level', 'city', 'salary_from', 'salary_to', 'is_internship', 'is_active', 'created_at']
    list_filter = ['level', 'type', 'city', 'is_internship', 'is_active', 'created_at']
    search_fields = ['title', 'description', 'city']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 30

@admin.register(InternshipPeriod)
class InternshipPeriodAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'application_deadline', 'max_participants', 'current_participants', 'is_active']
    list_filter = ['is_active', 'start_date']
    search_fields = ['name', 'description']
    list_per_page = 20

@admin.register(VacancyInternshipPeriod)
class VacancyInternshipPeriodAdmin(admin.ModelAdmin):
    list_display = ['vacancy', 'internship_period', 'available_slots', 'filled_slots', 'remaining_slots']
    list_filter = ['internship_period']
    search_fields = ['vacancy__title', 'internship_period__name']
    list_per_page = 20