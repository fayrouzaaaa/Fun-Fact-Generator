from django.urls import path
from . import views
urlpatterns = [
    path('allFunFacts/', views.display, name="allFacts"),
    path('allFunFacts/<int:pk>', views.delete, name="delete"),
]