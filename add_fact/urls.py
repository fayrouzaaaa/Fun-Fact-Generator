from django.urls import path
from . import views

urlpatterns=[
    path('addFunFact/', views.addButton),
    path('', views.generate_fact, name=""),
]