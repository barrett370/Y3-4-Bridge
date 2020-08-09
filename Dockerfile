FROM python:3
EXPOSE 8000
COPY . /site 
RUN pip install pipenv
WORKDIR /site
RUN pipenv install 
#RUN DJANGO_SETTINGS_MODULE=bridgesite.dev_settings pipenv run python manage.py migrate --run-syncdb
ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
