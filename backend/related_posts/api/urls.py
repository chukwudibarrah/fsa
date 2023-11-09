from django.urls import path
from .views import RelatedPostList
from rest_framework.routers import DefaultRouter


# related_post_router = DefaultRouter
# related_post_router.register(r'related_posts', RelatedPostList)


urlpatterns = [
    path('related-posts/', RelatedPostList.as_view(), name='related-post-list'),
]
