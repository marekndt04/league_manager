build:
	docker-compose build web

runserver:
	docker-compose run --rm --service-ports web ./manage.py runserver 0.0.0.0:8000

tests:
	docker-compose run --rm web pytest $(args)
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
	docker-compose run web pip install -r requirements/local.txt

reqs:
	docker-compose run --rm web pip-compile requirements/local.in
	docker-compose run --rm web pip-compile requirements/production.in
	docker-compose run --rm web pip-compile requirements/test.in
