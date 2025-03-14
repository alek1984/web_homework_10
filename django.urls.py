from django.urls import path
from .views import quotes_by_tag

urlpatterns += [
    path('tag/<str:tag>/', quotes_by_tag, name='quotes_by_tag'),
]
