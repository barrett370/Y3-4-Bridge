
.PHONY deps:
deps:
	pipenv install


.PHONY site:
site:
	python manage.py runserver 0.0.0.0:8000

.PHONY docker:
docker:
	sudo docker build -t sam/bridge_site .


.PHONY migrations:
migrations:
	DJANGO_SETTINGS_MODULE=bridgesite.test_settings pipenv run python manage.py makemigrations
	DJANGO_SETTINGS_MODULE=bridgesite.test_settings pipenv run python manage.py migrate


.PHONY unit:
unit:
	DJANGO_SETTINGS_MODULE=bridgesite.test_settings pipenv run python manage.py test blog.unit_tests


.PHONY func:
func:
	DJANGO_SETTINGS_MODULE=bridgesite.test_settings pipenv run python manage.py test blog.selenium_tests

.PHONY test:
test:
	make unit && make func 
	
.PHONY dev: 
dev: 
	DJANGO_SETTINGS_MODULE=bridgesite.test_settings make site
