install:
	pip install pip-tools && pip-sync
freeze:
	pip-compile requirements.in
run:
	python src/manage.py runserver
superuser:
	python src/manage.py createsuperuser
migrations:
	python src/manage.py makemigrations
migrate:
	python src/manage.py migrate
shell:
	python src/manage.py shell
lint:
	isort src/ && flake8 src/
test:
	pytest -svv src/
check-deploy:
	python manage.py check --deploy
