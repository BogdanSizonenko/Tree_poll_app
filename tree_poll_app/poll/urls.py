from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import HomeViewSet

router = DefaultRouter()

urlpatterns = [
    path('tests', HomeViewSet.as_view({'get': 'list'}), name='tests'),
    path('tests/<pk>', HomeViewSet.as_view({'get': 'retrieve'}), name='test'),
    path('tests/<pk>', HomeViewSet.as_view({'post': 'post'}), name='test'),
    path('tests/statistic/<pk>', HomeViewSet.as_view({'get': 'statistic'}), name='test'),
]

urlpatterns += router.urls