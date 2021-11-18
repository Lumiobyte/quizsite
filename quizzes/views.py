from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Quiz, Question, Choice

import random

# Create your views here.


def pogging(request):
    return render(request, 'quizzes/pogging.html', {"variable": random.choice(['Pogging', 'Gaming', 'Winning', 'Vibing'])})

def home_view(request):
    quizzes = []

    for quiz in Quiz.objects.all():
        quizzes.append(quiz)

    return render(request, 'quizzes/home.html', {"request": request, "quizzes": quizzes})

def do_quiz(request, slug):

    quiz = Quiz.objects.get(slug = slug)

    questions = {"titleimg": quiz.img, "titlename": quiz.name, "titledesc": quiz.description, "questioncount": quiz.num_questions, "questions": {}}

    print(Question.objects.get(quiz = quiz))

    for question in Question.objects.get(quiz = quiz):
        questions["questions"][str(question)] = {"img": question.img, "answers": {}}

        for choice in Choice.objects.all(question = question):
            questions["questions"][str(question)]["answers"][str(choice)] = {"correct": choice.correct}


    questionsList = []

    for question in Question.objects.get(quiz = quiz):
        questionsList.append(question)

    return render(request, 'quizzes/do_quiz.html', {"request": request, "quiz": questions, "questionsList": questionsList, "choiceModel": Choice})

@login_required()
def create_quiz(request):
    return render(request, 'quizzes/create_quiz.html', {"request": request})