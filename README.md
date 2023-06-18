instalace venv:

    py -3 -m venv venv

aktivace venv:

    source ./venv/Scripts/activate


instalace requirements.txt:

    pip install -r requirements.txt


naplnění databáze daty:

    py manage.py loadata fixtures/*

    py manage.py dumpdata --format yaml [typeName]


spuštění projektu (v adresáři gamdb):

    python manage.py runserver


otevření projektu v prohlížeči:
    localhost:8000


Po upravení models.py nebo admin.py (v adresáři gamdb):

    python manage.py makemigrations

    python manage.py migrate