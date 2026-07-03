from django.urls import path
from . import views

urlpatterns = [
    path('generateFunFact/', views.generate, name="generateFact"),
    path('addFunFact/', views.add_fact, name="addFact"),
    path('generateFunFact/<int:pk>', views.likeButton, name = "likeButton")
]