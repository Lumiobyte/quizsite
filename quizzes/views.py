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

    if request.method == "POST":

        answers = list(request.POST.values())
        print(answers)
        counter = 1

        correctOrNotCorrect = []
        totalCorrect = 0
        totalWrong = 0

        for question in Question.objects.filter(quiz = quiz):
            getOptionMapping = {'0': question.op0, '1': question.op1, '2': question.op2, '3': question.op3}

            if answers[counter] == question.ans:
                correctOrNotCorrect.append("<strong>{}</strong> was correct!".format(getOptionMapping[question.ans]))
                totalCorrect += 1
            else:
                totalWrong += 1
                correctOrNotCorrect.append("Incorrect. Correct answer was <strong>{}</strong>".format(getOptionMapping[question.ans]))

            counter += 1

        print(correctOrNotCorrect)

        return render(request, 'quizzes/results.html', {"request": request, "quiz": quiz, "correctOrNotCorrect": correctOrNotCorrect, "totalCorrect": totalCorrect, "totalWrong": totalWrong, "totalQuestions": counter - 1, "percentScore": round(totalCorrect / (counter - 1) * 100, 2)})
    else:
        quizInfo = {"titleimg": quiz.img, "titlename": quiz.name, "titledesc": quiz.description, "questioncount": quiz.num_questions}

        questionsList = []
        for question in Question.objects.filter(quiz = quiz):
            questionsList.append(question)

        return render(request, 'quizzes/do_quiz.html', {"request": request, "quiz": quizInfo, "questionsList": questionsList, "choiceModel": Choice})

@login_required()
def create_quiz(request):
    return render(request, 'quizzes/create_quiz.html', {"request": request})