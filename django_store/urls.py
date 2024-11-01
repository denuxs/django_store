from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.viewsets import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
