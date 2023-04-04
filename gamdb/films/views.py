from django.shortcuts import render
from .models import Movie, Director


def homepage(request):
    context = {
        'movies': Movie.objects.all()
    }
    return render(request, 'main.html', context)
    # return HttpResponse("hee hee")


def directors(request):
    context = {
        'title': 'Reziseri',
        'directors': Director.objects.all(),
    }
    return render(request, 'directors.html', context)