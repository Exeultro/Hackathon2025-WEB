from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (VacancyViewSet, InternshipPeriodViewSet, ApplicationViewSet,
                   NewsViewSet, TeamMemberViewSet, SimulatorTaskViewSet, SimulatorProgressViewSet)

router = DefaultRouter()
router.register(r'vacancies', VacancyViewSet, basename='vacancy')
router.register(r'internship-periods', InternshipPeriodViewSet, basename='internship-period')
router.register(r'applications', ApplicationViewSet, basename='application')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'team-members', TeamMemberViewSet, basename='team-member')
router.register(r'simulator-tasks', SimulatorTaskViewSet, basename='simulator-task')
router.register(r'simulator-progress', SimulatorProgressViewSet, basename='simulator-progress')
urlpatterns = [
    path('', include(router.urls)),
]