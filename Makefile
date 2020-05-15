include .env

.PHONY: frontend
frontend:
	cd frontend/web && npm run dev

.PHONY: backend
backend:
	pipenv run ./backend/manage.py runserver --settings=backend.settings.dev 
