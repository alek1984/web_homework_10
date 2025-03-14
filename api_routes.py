from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, QuoteViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'quotes', QuoteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
