# vacancies/admin_views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Vacancy, InternshipPeriod, Application, News, TeamMember, SimulatorTask
from .serializers import *

class AdminApplicationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Application.objects.all().select_related('vacancy')
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status', 'application_type']
    search_fields = ['first_name', 'last_name', 'email', 'vacancy__title']
    
    def get_queryset(self):
        # Оптимизация запроса
        return Application.objects.all().select_related('vacancy').only(
            'id', 'first_name', 'last_name', 'email', 'status', 
            'submitted_at', 'vacancy__title'
        )

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        application = self.get_object()
        new_status = request.data.get('status')
        
        if new_status in dict(Application.STATUS_CHOICES):
            application.status = new_status
            application.save()
            
            return Response({
                'status': 'success',
                'message': f'Статус заявки обновлен на "{application.get_status_display()}"'
            })
        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)

class AdminNewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['is_published']
    search_fields = ['title', 'content']
    
    def get_queryset(self):
        # Оптимизация - выбираем только нужные поля
        return News.objects.all().only(
            'id', 'title', 'is_published', 'published_at', 'created_at'
        )

    @action(detail=True, methods=['post'])
    def toggle_publish(self, request, pk=None):
        news = self.get_object()
        news.is_published = not news.is_published
        news.save()
        return Response({
            'status': 'success',
            'is_published': news.is_published,
            'message': f'Новость {"опубликована" if news.is_published else "снята с публикации"}'
        })

# Остальные ViewSet можно удалить или оставить по необходимости

class AdminApplicationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'application_type', 'vacancy', 'internship_period']
    search_fields = ['first_name', 'last_name', 'email', 'vacancy__title']
    ordering_fields = ['submitted_at', 'created_at']
    ordering = ['-submitted_at']

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        application = self.get_object()
        new_status = request.data.get('status')
        
        if new_status in dict(Application.STATUS_CHOICES):
            application.status = new_status
            if new_status == Application.STATUS_REVIEWED:
                application.reviewed_at = timezone.now()
            application.save()
            
            return Response({
                'status': 'success',
                'message': f'Статус заявки обновлен на "{application.get_status_display()}"'
            })
        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)

class AdminNewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_published']
    search_fields = ['title', 'content', 'preview']
    ordering_fields = ['published_at', 'created_at']
    ordering = ['-published_at']

    @action(detail=True, methods=['post'])
    def toggle_publish(self, request, pk=None):
        news = self.get_object()
        news.is_published = not news.is_published
        news.save()
        return Response({
            'status': 'success',
            'is_published': news.is_published,
            'message': f'Новость {"опубликована" if news.is_published else "снята с публикации"}'
        })

class AdminTeamMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active', 'city']
    search_fields = ['first_name', 'last_name', 'position', 'education']
    ordering_fields = ['display_order', 'experience_years', 'created_at']
    ordering = ['display_order']

    @action(detail=True, methods=['post'])
    def toggle_status(self, request, pk=None):
        member = self.get_object()
        member.is_active = not member.is_active
        member.save()
        return Response({
            'status': 'success',
            'is_active': member.is_active,
            'message': f'Участник {"активирован" if member.is_active else "деактивирован"}'
        })

class AdminInternshipPeriodViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = InternshipPeriod.objects.all()
    serializer_class = InternshipPeriodSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['start_date', 'end_date', 'created_at']
    ordering = ['-start_date']

    @action(detail=True, methods=['post'])
    def toggle_status(self, request, pk=None):
        period = self.get_object()
        period.is_active = not period.is_active
        period.save()
        return Response({
            'status': 'success',
            'is_active': period.is_active,
            'message': f'Период практики {"активирован" if period.is_active else "деактивирован"}'
        })

class AdminSimulatorTaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = SimulatorTask.objects.all()
    serializer_class = SimulatorTaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['profession_type', 'difficulty', 'is_active', 'level']
    search_fields = ['title', 'description', 'problem']
    ordering_fields = ['level', 'difficulty', 'estimated_time', 'created_at']
    ordering = ['profession_type', 'level', 'difficulty']

    @action(detail=True, methods=['post'])
    def toggle_status(self, request, pk=None):
        task = self.get_object()
        task.is_active = not task.is_active
        task.save()
        return Response({
            'status': 'success',
            'is_active': task.is_active,
            'message': f'Задача {"активирована" if task.is_active else "деактивирована"}'
        })