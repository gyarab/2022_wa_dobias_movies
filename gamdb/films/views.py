from django.shortcuts import render

from .models import Director, Movie


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

def movies(request):
    context = {
        'title': 'Filmy',
        'movies': Movie.objects.all(),
    }
    return render(request, 'movies.html', context)

def movie(request, id):
    context = {
        'title': 'Film',
        'movie': Movie.objects.get(pk=id),
    }
    return render(request, 'movie.html', context)