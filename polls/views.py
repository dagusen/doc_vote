from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.forms.formsets import formset_factory

from polls.models import Question, Choice
from .forms import QuestionModelForm, ChoiceModelForm, ChoiceFormSet


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


@login_required(login_url="/user/login")
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


def create(request):
    ChoiceForm = formset_factory(ChoiceModelForm, max_num=10, formset=ChoiceFormSet)
    QuestionForm = QuestionModelForm(None)
    if request.method == "POST":
        QuestionForm = QuestionModelForm(request.POST)
        ChoiceForm = ChoiceForm(request.POST)
        if ChoiceForm.is_valid() and QuestionForm.is_valid():
            question = QuestionForm.save()
            for form in ChoiceForm.forms:
                question.choice_set.create(choice_text=form.cleaned_data['choice_text'])
            return redirect("polls:detail", poll_id=question.id)
        else:
            return render(request, "polls/create.html", {"question_form": QuestionForm, "choice_forms": ChoiceForm})

    return render(request, "polls/create.html", {
        "question_form": QuestionForm,
        "choice_forms": ChoiceForm
    })
