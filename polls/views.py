from django.shortcuts import render
from polls.models import Question, Choice


def index(request):
    polls = Question.objects.all()
    return render(request, "polls/index.html", {"polls": polls})
