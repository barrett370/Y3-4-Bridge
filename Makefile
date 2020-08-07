.PHONY deps:
deps:
	pipenv install


.PHONY site:
site:
	python manage.py runserver 
