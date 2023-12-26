run:
	docker-compose up -d

test:
	docker-compose exec -it api pytest

restart:
	docker-compose restart api

migrations:
	docker-compose exec -it api python manage.py makemigrations

migrate:
	docker-compose exec -it api python manage.py migrate