
from django.shortcuts import render, redirect
from .models import People
from .forms import PeopleForm

# Create your views here.


def index(request):
    error = ''
    if request.method == 'POST':
        form = PeopleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            error = 'Форма была неверной'

    form = PeopleForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/index.html', context)


def list(request):
    people = People.objects.order_by('date_of_birth')
    return render(request, 'main/list.html', {'title': 'List', 'people': people})
