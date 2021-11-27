runserver:
	docker-compose run --rm web ./manage.py runserver

super_user:
	docker-compose run --rm web ./manage.py createsuperuser

migrations:
	docker-compose run --rm web ./manage.py makemigrations

migrate:
	docker-compose run --rm web ./manage.py migrate

cli:
	docker-compose run --rm web bash
