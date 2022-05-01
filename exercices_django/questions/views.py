from django.shortcuts import render, redirect
from .models import Question

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'questions/index.html', context)

def add(request):
    return render(request, 'questions/add.html')

def insert(request):
    text = request.POST.get('text')
    question = Question(text=text)
    question.save()
    return redirect('questions:index')

def edit(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {'question': question}
    return render(request, 'questions/edit.html', context)

def update(request, question_id):
    question = Question.objects.get(pk=question_id)
    question.text = request.POST.get('text')
    question.save()
    return redirect('questions:index')

def delete(request, question_id):
    question = Question.objects.get(pk=question_id)
    question.delete()
    return redirect('questions:index')