from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('delete/<int:course_id>', views.delete),
    path('comment/<int:course_id>', views.comment),
    path('comment/create/<int:course_id>', views.createcomment),
]