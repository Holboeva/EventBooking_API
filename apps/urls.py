from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EventViewSet, RegistrationViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('events', EventViewSet)
router.register('registrations', RegistrationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

