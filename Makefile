
.PHONY deps:
deps:
	pipenv install


.PHONY site:
site:
	python manage.py runserver 0.0.0.0:8000

.PHONY docker:
docker:
	sudo docker build -t sam/bridge_site .



.PHONY test:
	DJANGO_SETTINGS_MODULE=bridgesite.test_settings pipenv run python manage.py test blog
