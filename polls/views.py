from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from polls.models import Question, Choice


def index(request):
    polls = Question.objects.all().order_by('-id')
    paginator = Paginator(polls, 5)
    page = request.GET.get('page')

    try:
        polls = paginator.page(page)
    except PageNotAnInteger:
        polls = paginator.page(1)
    except EmptyPage:
        polls = paginator.page(paginator.num_pages)

    return render(request, "polls/index.html", {"polls": polls})


def results(request):
    polls = Question.objects.all()
    return render(request, "polls/results.html", {"polls": polls})


def detail(request, poll_id):
    try:
        poll = Question.objects.get(pk=poll_id)
    except Question.DoesNotExist:
        raise Http404("Sorry Poll Doesn't Found")

    return render(request, "polls/detail.html", {"poll": poll})


def vote(request, poll_id):
    poll = get_object_or_404(Question, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(id=request.POST['vote'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "poll": poll,
            "error_message": "You Didn't Choice Any Option :("
        })

    selected_choice.votes += 1
    selected_choice.save()

    return redirect("polls:detail", poll_id=poll.id)


def result(request, poll_id):
    poll = get_object_or_404(Question, pk=poll_id)
    return render(request, "polls/result.html", {"poll": poll})
