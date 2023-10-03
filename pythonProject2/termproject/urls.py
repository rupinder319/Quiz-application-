from django.urls import path

from . import views
from .views import quiz_create

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),

    path('quiz/',views.quiz,name='quiz'),
    path('quiz/save/', views.quiz_create,name='quiz_create'),
    path('score/',views.submit_result,name='score'),
]