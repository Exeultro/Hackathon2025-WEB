from rest_framework import serializers
from .models import Vacancy, User, InternshipPeriod, VacancyInternshipPeriod, Application, News, TeamMember, SimulatorTask, SimulatorProgress

class InternshipPeriodSerializer(serializers.ModelSerializer):
    available_slots = serializers.ReadOnlyField()
    
    class Meta:
        model = InternshipPeriod
        fields = '__all__'

class VacancyInternshipPeriodSerializer(serializers.ModelSerializer):
    internship_period = InternshipPeriodSerializer(read_only=True)
    remaining_slots = serializers.ReadOnlyField()
    
    class Meta:
        model = VacancyInternshipPeriod
        fields = '__all__'

class VacancyListSerializer(serializers.ModelSerializer):
    salary = serializers.ReadOnlyField()
    internship_periods = serializers.SerializerMethodField()
    
    class Meta:
        model = Vacancy
        fields = [
            'id', 'title', 'level', 'type', 'city', 
            'salary_from', 'salary_to', 'salary_comment', 'salary',
            'description', 'full_description', 'requirements', 'responsibilities',
            'work_conditions', 'selection_process', 'benefits',
            'is_internship', 'application_count', 'applications_today',
            'total_applications', 'created_at', 'updated_at', 'internship_periods'
        ]

    def get_internship_periods(self, obj):
        if obj.is_internship:
            periods = VacancyInternshipPeriod.objects.filter(vacancy=obj)
            return VacancyInternshipPeriodSerializer(periods, many=True).data
        return []

class VacancyDetailSerializer(serializers.ModelSerializer):
    salary = serializers.ReadOnlyField()
    internship_periods = serializers.SerializerMethodField()
    
    class Meta:
        model = Vacancy
        fields = '__all__'

    def get_internship_periods(self, obj):
        if obj.is_internship:
            periods = VacancyInternshipPeriod.objects.filter(vacancy=obj)
            return VacancyInternshipPeriodSerializer(periods, many=True).data
        return []
    
class ApplicationSerializer(serializers.ModelSerializer):
    vacancy_title = serializers.CharField(source='vacancy.title', read_only=True)
    
    class Meta:
        model = Application
        fields = [
            'id', 'vacancy', 'vacancy_title', 'application_type', 'internship_period',
            'first_name', 'last_name', 'middle_name', 'email', 'phone', 'city',
            'education_institution', 'faculty', 'course', 
            'experience_description', 'motivation', 'resume_url',
            'status', 'submitted_at', 'created_at'
        ]
        read_only_fields = ['status', 'submitted_at', 'created_at']

    def create(self, validated_data):
        # Обработка поля course
        course = validated_data.get('course')
        if course == '' or course is None:
            validated_data['course'] = None
        
        return Application.objects.create(**validated_data)
    

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'id', 'title', 'content', 'preview', 'image_url',
            'is_published', 'published_at', 'created_at', 'updated_at'
        ]

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = [
            'id', 'first_name', 'last_name', 'position', 'city', 
            'education', 'bio', 'photo_url', 'email', 'phone',
            'experience_years', 'display_order', 'is_active', 'created_at'
        ]

class SimulatorTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimulatorTask
        fields = [
            'id', 'profession_type', 'level', 'title', 'difficulty',
            'estimated_time', 'description', 'problem', 'hint',
            'correct_answer', 'is_active', 'created_at'
        ]

class SimulatorProgressSerializer(serializers.ModelSerializer):
    task_title = serializers.CharField(source='task.title', read_only=True)
    profession_type = serializers.CharField(source='task.profession_type', read_only=True)
    
    class Meta:
        model = SimulatorProgress
        fields = [
            'id', 'user_email', 'task_id', 'task_title', 'profession_type',
            'completed', 'user_solution', 'is_correct', 'completed_at', 'created_at'
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'created_at']
        read_only_fields = ['created_at']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'role']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)  # В реальном приложении здесь было бы хеширование
        user.save()
        return user