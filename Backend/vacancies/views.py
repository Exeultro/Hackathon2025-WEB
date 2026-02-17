from django.utils import timezone
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Vacancy, InternshipPeriod, Application, News, TeamMember, SimulatorTask, SimulatorProgress
from .serializers import (VacancyListSerializer, VacancyDetailSerializer, 
                         InternshipPeriodSerializer, ApplicationSerializer,
                         NewsSerializer, TeamMemberSerializer, 
                         SimulatorTaskSerializer, SimulatorProgressSerializer)

class VacancyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vacancy.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['level', 'type', 'city', 'is_internship']
    search_fields = ['title', 'description', 'city', 'full_description']
    ordering_fields = ['created_at', 'salary_from', 'salary_to']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VacancyDetailSerializer
        return VacancyListSerializer

    @action(detail=False, methods=['get'])
    def filters(self, request):
        """Возвращает доступные фильтры для фронтенда"""
        vacancies = Vacancy.objects.filter(is_active=True)
        
        return Response({
            'levels': dict(Vacancy.LEVEL_CHOICES),
            'types': dict(Vacancy.TYPE_CHOICES),
            'cities': list(vacancies.values_list('city', flat=True).distinct()),
            'internship_status': [
                {'value': True, 'label': 'Стажировки'},
                {'value': False, 'label': 'Работа'}
            ]
        })

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Популярные вакансии"""
        featured_vacancies = self.get_queryset().order_by('-application_count')[:6]
        serializer = self.get_serializer(featured_vacancies, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def internships(self, request):
        """Только стажировки"""
        internships = self.get_queryset().filter(is_internship=True)
        serializer = self.get_serializer(internships, many=True)
        return Response(serializer.data)

class InternshipPeriodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InternshipPeriod.objects.filter(is_active=True)
    serializer_class = InternshipPeriodSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            application = serializer.save()
            
            # Обновляем счетчики вакансии
            vacancy = application.vacancy
            vacancy.applications_today += 1
            vacancy.application_count += 1
            vacancy.total_applications += 1
            vacancy.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.filter(is_published=True)
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'preview']
    ordering_fields = ['published_at', 'created_at']
    ordering = ['-published_at']

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Последние 3 новости для главной страницы"""
        featured_news = self.get_queryset()[:3]
        serializer = self.get_serializer(featured_news, many=True)
        return Response(serializer.data)
    
class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamMember.objects.filter(is_active=True)
    serializer_class = TeamMemberSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['display_order', 'experience_years']
    ordering = ['display_order']

    @action(detail=False, methods=['get'])
    def active(self, request):
        """Активные члены команды"""
        active_members = self.get_queryset()
        serializer = self.get_serializer(active_members, many=True)
        return Response(serializer.data)

class SimulatorTaskViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SimulatorTask.objects.filter(is_active=True)
    serializer_class = SimulatorTaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['profession_type', 'level', 'difficulty']
    ordering_fields = ['level', 'difficulty', 'estimated_time']
    ordering = ['profession_type', 'level', 'difficulty']

class SimulatorProgressViewSet(viewsets.ModelViewSet):
    queryset = SimulatorProgress.objects.all()
    serializer_class = SimulatorProgressSerializer
    
    def get_queryset(self):
        queryset = SimulatorProgress.objects.all()
        user_email = self.request.query_params.get('user_email')
        if user_email:
            queryset = queryset.filter(user_email=user_email)
        return queryset

    def create(self, request, *args, **kwargs):
        # Проверяем, есть ли уже прогресс для этой задачи
        user_email = request.data.get('user_email')
        task_id = request.data.get('task_id')
        
        if user_email and task_id:
            existing_progress = SimulatorProgress.objects.filter(
                user_email=user_email, 
                task_id=task_id
            ).first()
            
            if existing_progress:
                # Обновляем существующую запись
                serializer = self.get_serializer(existing_progress, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
        
        # Создаем новую запись
        return super().create(request, *args, **kwargs)