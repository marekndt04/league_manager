build:
	docker-compose build web

runserver:
	docker-compose run --rm --service-ports web

super_user:
	docker-compose run --rm web ./manage.py createsuperuser

migrations:
	docker-compose run --rm web ./manage.py makemigrations

migrate:
	docker-compose run --rm web ./manage.py migrate

cli:
	docker-compose run --rm web bash

shell:
	docker-compose run web /bin/bash

install_reqs:
	pip install -r requirements/local.txt

reqs:
	pip-compile requirements/local.in
	pip-compile requirements/production.in
	pip-compile requirements/test.in
