from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from djangoapp.gitapp.views import UserView, RepositoryView

router = DefaultRouter()
router.register('users', UserView)
router.register('repository', RepositoryView)

urlpatterns = [
    path('', include(router.urls))
]