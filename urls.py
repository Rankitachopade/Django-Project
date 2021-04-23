from django.urls import path
from . import views

urlpatterns = [
# path('', views.index, name="index"),
 path('', views.quiz_view, name="about"),
 ]