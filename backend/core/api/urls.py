from django.urls import include, path
from rest_framework.routers import DefaultRouter
from posts.api.urls import post_router
from projects.api.urls import project_router
from related_posts.api.urls import urlpatterns as related_posts_urls

router = DefaultRouter()

router.registry.extend(post_router.registry)
router.registry.extend(project_router.registry)

urlpatterns = [
    path('', include(router.urls)),
    path('related_posts/', include(related_posts_urls)),
]
