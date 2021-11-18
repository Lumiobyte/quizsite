from django.urls import path
from . import views

urlpatterns = [
    path('pogging/', views.pogging),
    path('<str:slug>/', views.do_quiz),
    path('', views.home_view)
]