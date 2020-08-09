
.PHONY deps:
deps:
	pipenv install


.PHONY site:
site:
	python manage.py runserver 0.0.0.0:8000

.PHONY docker:
docker:
	sudo docker build -t sam/bridge_site .


.PHONY prod:
prod:
	make docker && sudo docker run -p 8000:8000 -e "DJANGO_SETTINGS_MODULE=bridgesite.prod_settings" sam/bridge_site:latest 

.PHONY dev:
dev:
	make docker && sudo docker run -p 8000:8000 -e "DJANGO_SETTINGS_MODULE=bridgesite.dev_settings" sam/bridge_site:latest 
