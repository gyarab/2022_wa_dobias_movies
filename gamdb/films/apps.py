from django.apps import AppConfig


class FilmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'films'

class ActorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'actors'

class DirectorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'directors'

class CommentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comments'

class GenresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'genres'

