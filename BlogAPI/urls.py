from django.conf.urls import url
from rest_framework import routers
from .views import UserViewSet, Blog_PostViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'blog', Blog_PostViewSet)

urlpatterns = router.urls