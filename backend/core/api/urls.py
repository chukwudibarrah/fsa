from rest_framework.routers import DefaultRouter
from posts.api.urls import post_router
from projects.api.urls import project_router
from django.urls import path, include

router = DefaultRouter()

router.registry.extend(post_router.registry)
router.registry.extend(project_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
