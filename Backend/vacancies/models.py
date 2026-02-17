from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Vacancy(models.Model):
    LEVEL_INTERN = 'intern'
    LEVEL_JUNIOR = 'junior' 
    LEVEL_MIDDLE = 'middle'
    LEVEL_SENIOR = 'senior'
    LEVEL_LEAD = 'lead'
    
    LEVEL_CHOICES = [
        (LEVEL_INTERN, 'Стажировка'),
        (LEVEL_JUNIOR, 'Junior'),
        (LEVEL_MIDDLE, 'Middle'),
        (LEVEL_SENIOR, 'Senior'),
        (LEVEL_LEAD, 'Team Lead'),
    ]
    
    TYPE_ONSITE = 'onsite'
    TYPE_REMOTE = 'remote'
    TYPE_HYBRID = 'hybrid'
    
    TYPE_CHOICES = [
        (TYPE_ONSITE, 'Очная'),
        (TYPE_REMOTE, 'Удаленная'),
        (TYPE_HYBRID, 'Гибрид'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название вакансии")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, verbose_name="Уровень")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Тип работы")
    city = models.CharField(max_length=100, verbose_name="Город")
    salary_from = models.IntegerField(null=True, blank=True, verbose_name="Зарплата от")
    salary_to = models.IntegerField(null=True, blank=True, verbose_name="Зарплата до")
    salary_comment = models.CharField(max_length=100, blank=True, verbose_name="Комментарий к зарплате")
    description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(blank=True, verbose_name="Полное описание")
    
    # JSON поля для хранения списков
    requirements = models.JSONField(default=list, verbose_name="Требования")
    responsibilities = models.JSONField(default=list, verbose_name="Обязанности")
    work_conditions = models.JSONField(default=list, verbose_name="Условия работы")
    selection_process = models.JSONField(default=list, verbose_name="Процесс отбора")
    benefits = models.JSONField(default=list, verbose_name="Бонусы")
    
    is_internship = models.BooleanField(default=False, verbose_name="Стажировка")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    application_count = models.IntegerField(default=0, verbose_name="Количество откликов")
    applications_today = models.IntegerField(default=0, verbose_name="Откликов сегодня")
    total_applications = models.IntegerField(default=0, verbose_name="Всего откликов")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        db_table = 'vacancies'
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.city})"

    @property
    def salary(self):
        if self.salary_from and self.salary_to:
            return f"от {self.salary_from} до {self.salary_to} ₽"
        elif self.salary_from:
            return f"от {self.salary_from} ₽"
        elif self.salary_to:
            return f"до {self.salary_to} ₽"
        else:
            return "по договоренности"

class InternshipPeriod(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название периода")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    application_deadline = models.DateField(verbose_name="Дедлайн подачи")
    max_participants = models.IntegerField(verbose_name="Максимум участников")
    current_participants = models.IntegerField(default=0, verbose_name="Текущее количество участников")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'internship_periods'
        verbose_name = 'Период практики'
        verbose_name_plural = 'Периоды практики'
        ordering = ['-start_date']

    def __str__(self):
        return self.name

    @property
    def available_slots(self):
        return self.max_participants - self.current_participants

class VacancyInternshipPeriod(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name="Вакансия")
    internship_period = models.ForeignKey(InternshipPeriod, on_delete=models.CASCADE, verbose_name="Период практики")
    available_slots = models.IntegerField(verbose_name="Доступные места")
    filled_slots = models.IntegerField(default=0, verbose_name="Занятые места")

    class Meta:
        db_table = 'vacancy_internship_periods'
        verbose_name = 'Связь вакансии и периода практики'
        verbose_name_plural = 'Связи вакансий и периодов практики'
        unique_together = ['vacancy', 'internship_period']

    def __str__(self):
        return f"{self.vacancy.title} - {self.internship_period.name}"

    @property
    def remaining_slots(self):
        return self.available_slots - self.filled_slots
    
class Application(models.Model):
    STATUS_NEW = 'NW'
    STATUS_REVIEWED = 'RV' 
    STATUS_ACCEPTED = 'AC'
    STATUS_REJECTED = 'RJ'
    
    STATUS_CHOICES = [
        (STATUS_NEW, 'Новая'),
        (STATUS_REVIEWED, 'Рассмотрена'),
        (STATUS_ACCEPTED, 'Принята'),
        (STATUS_REJECTED, 'Отклонена'),
    ]

    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name="Вакансия")
    application_type = models.CharField(max_length=20, choices=[('regular', 'Обычная'), ('internship', 'Практика')], verbose_name="Тип заявки")
    internship_period = models.ForeignKey(InternshipPeriod, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Период практики")
    
    # Персональные данные
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, blank=True, verbose_name="Отчество")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    city = models.CharField(max_length=100, verbose_name="Город")
    
    # Образовательная информация (для практики)
    education_institution = models.CharField(max_length=255, blank=True, verbose_name="Учебное заведение")
    faculty = models.CharField(max_length=255, blank=True, verbose_name="Факультет")
    course = models.IntegerField(null=True, blank=True, verbose_name="Курс")    
    # Профессиональная информация
    experience_description = models.TextField(blank=True, verbose_name="Опыт работы")
    motivation = models.TextField(verbose_name="Мотивация")
    resume_url = models.URLField(blank=True, verbose_name="Ссылка на резюме")
    
    # Статус заявки
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=STATUS_NEW, verbose_name="Статус")
    
    # Даты
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подачи")
    reviewed_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата рассмотрения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'applications'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.last_name} {self.first_name} - {self.vacancy.title}"

# ✅ ДОБАВЛЯЕМ НОВЫЕ МОДЕЛИ

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    preview = models.TextField(verbose_name="Превью")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL изображения")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    published_at = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        db_table = 'news'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    position = models.CharField(max_length=255, verbose_name="Должность")
    city = models.CharField(max_length=100, verbose_name="Город")
    education = models.CharField(max_length=255, verbose_name="Образование")
    bio = models.TextField(verbose_name="Биография")
    photo_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL фото")
    email = models.EmailField(blank=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    experience_years = models.IntegerField(default=0, verbose_name="Лет опыта")
    display_order = models.IntegerField(default=0, verbose_name="Порядок отображения")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'team_members'
        verbose_name = 'Член команды'
        verbose_name_plural = 'Члены команды'
        ordering = ['display_order', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

class SimulatorTask(models.Model):
    PROFESSION_PROGRAMMER = 'programmer'
    PROFESSION_CONSULTANT = 'consultant'
    PROFESSION_SERVICE = 'service'
    
    PROFESSION_CHOICES = [
        (PROFESSION_PROGRAMMER, 'Программист'),
        (PROFESSION_CONSULTANT, 'Консультант'),
        (PROFESSION_SERVICE, 'Сервисный инженер'),
    ]
    
    DIFFICULTY_BEGINNER = 'beginner'
    DIFFICULTY_INTERMEDIATE = 'intermediate'
    DIFFICULTY_ADVANCED = 'advanced'
    
    DIFFICULTY_CHOICES = [
        (DIFFICULTY_BEGINNER, 'Начинающий'),
        (DIFFICULTY_INTERMEDIATE, 'Средний'),
        (DIFFICULTY_ADVANCED, 'Продвинутый'),
    ]

    profession_type = models.CharField(max_length=50, choices=PROFESSION_CHOICES, verbose_name="Тип профессии")
    level = models.IntegerField(verbose_name="Уровень")
    title = models.CharField(max_length=255, verbose_name="Название задачи")
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES, verbose_name="Сложность")
    estimated_time = models.IntegerField(verbose_name="Примерное время (минуты)")
    description = models.TextField(verbose_name="Описание")
    problem = models.TextField(verbose_name="Постановка задачи")
    hint = models.TextField(verbose_name="Подсказка")
    correct_answer = models.TextField(verbose_name="Правильный ответ")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'simulator_tasks'
        verbose_name = 'Задача симулятора'
        verbose_name_plural = 'Задачи симулятора'
        ordering = ['profession_type', 'level', 'difficulty']

    def __str__(self):
        return f"{self.title} ({self.get_profession_type_display()})"

class SimulatorProgress(models.Model):
    user_email = models.EmailField(verbose_name="Email пользователя")
    task = models.ForeignKey(SimulatorTask, on_delete=models.CASCADE, verbose_name="Задача")
    completed = models.BooleanField(default=False, verbose_name="Выполнено")
    user_solution = models.TextField(blank=True, verbose_name="Решение пользователя")
    is_correct = models.BooleanField(null=True, blank=True, verbose_name="Правильно")
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата выполнения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'simulator_progress'
        verbose_name = 'Прогресс симулятора'
        verbose_name_plural = 'Прогресс симулятора'
        unique_together = ['user_email', 'task']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user_email} - {self.task.title}"
    
class User(models.Model):
    ROLE_ADMIN = 'admin'
    ROLE_MODERATOR = 'moderator'
    ROLE_USER = 'user'
    
    ROLE_CHOICES = [
        (ROLE_ADMIN, 'Администратор'),
        (ROLE_MODERATOR, 'Модератор'),
        (ROLE_USER, 'Пользователь'),
    ]

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_USER)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"