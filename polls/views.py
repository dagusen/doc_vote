from django.shortcuts import render
from django.http import Http404
from polls.models import Question, Choice


def index(request):
    polls = Question.objects.all()
    return render(request, "polls/index.html", {"polls": polls})


def detail(request, poll_id):
    try:
        poll = Question.objects.get(pk=poll_id)
    except Question.DoesNotExist:
        raise Http404("Sorry Poll Doesn't Found")

    return render(request, "polls/detail.html", {"poll": poll})
