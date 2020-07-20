from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    context = {
        'courses': Course.objects.all() 
    }
    return render(request, 'index.html', context)

def create(request):
    errors = Course.objects.validate(request.POST)
    if errors:
        for field, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        course = Course.objects.create(
            name=request.POST['name'],
        
        description = Description.objects.create(
            content=request.POST['content'],
        ))
        return redirect('/')

def delete(request, course_id):
    if request.method == "GET":
        context = {
            'course': Course.objects.get(id=course_id)
        }
        return render(request, 'delete.html', context)
    if request.method == "POST":
        course = Course.objects.get(id=course_id)
        course.delete()
        return redirect('/')

def comment(request, course_id):
    context = {
        'courses': Course.objects.get(id=course_id)
    }
    return render(request, 'comment.html', context)

def createcomment(request, course_id):
    Comment.objects.create(
        comment=request.POST['comment'],
        course = Course.objects.get(id=course_id),
    )
    return redirect(f'/comment/{course_id}')