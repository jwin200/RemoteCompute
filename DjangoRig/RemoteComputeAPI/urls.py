from django.urls import path, include
from rest_framework import routers
from .views import ExecutableViewSet, container_view

router = routers.DefaultRouter()
router.register(r'executables', ExecutableViewSet)
# Automatic URL routing
urlpatterns = [
    path('', include(router.urls)),
    path('upload/', container_view),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
