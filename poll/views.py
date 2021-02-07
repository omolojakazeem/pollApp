from django.shortcuts import render, redirect, HttpResponse
from .forms import PollForm
from .models import Poll


def home(request):
    template = 'poll/home.html'
    polls = Poll.objects.all()
    context = {
        'polls': polls

    }
    return render(request, template_name=template, context=context)


def create(request):
    template = 'poll/create.html'

    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PollForm()
    context = {
        'form': form,
    }

    return render(request, template_name=template, context=context)


def result(request, poll_id):
    template = 'poll/results.html'
    poll = Poll.objects.get(id=poll_id)

    context = {
        'poll': poll,
    }

    return render(request, template_name=template, context=context)


def vote(request, poll_id):
    template = 'poll/vote.html'
    poll = Poll.objects.get(id=poll_id)

    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, "Invalid Form")
        poll.save()
        return redirect('results', poll.id)
    context = {
        'poll': poll,
    }

    return render(request, template_name=template, context=context)
