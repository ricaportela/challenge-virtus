Chanlenge Virtus
=========================

PYTHON Project with Django and Django Restful Framework


How to install in locally (supposing you have git and python >= 3.6 installed):

```console
git clone https://github.com/challenge-virtus.git
cd challenge-virtus
cp contrib/env-sample .env
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

If you want use SQLite on your dev environment, please remove DATABASE_URL from .env file.
Otherwise fill this value with your database credentials.

You can aply migrations to generate database schema:

```console
python manage.py migrate
``` 

You can also create a user:

```console
python manage.py createsuperuser
```

To run server locally (with virtualenv activated):

```console
python manager.py runserver
```

If you want populate the database with some content run: 

```console
python manage.py loaddata virtus_contents
```

To tun the tests:

```console
pytest virtus
```

If you want run your amb dev using postgres, you can install docker and run:

```console
docker run -p 5432:5432 --env POSTGRES_PASSWORD=pass --name virtus-postgres -d postgres:9
```

and add to your .env

```console
DATABASE_URL=postgres://postgres:pass@localhost:5432/postgres
```


#License Details

The AGPL license here cover everything relate to source code.


Enjoy!

