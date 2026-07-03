from django.urls import path
from . import views

urlpatterns=[
    path('likedFunFacts/', views.likedFacts, name="likedFacts"),
    path('likedFunFacts/<int:pk>', views.unlike, name="unlike")
]