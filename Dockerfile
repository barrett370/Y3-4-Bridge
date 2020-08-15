FROM python:3
EXPOSE 8000
COPY . /site 
RUN pip install pipenv
WORKDIR /site
RUN pipenv install 
ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
