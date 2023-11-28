from django.urls import path, include

urlpatterns = [
    path('authors/', include('api.v1.authors')),
]
