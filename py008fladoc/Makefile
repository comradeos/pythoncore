include .env
export

COMPOSE=docker compose

.PHONY: build up down clean start stop

build:
	$(COMPOSE) build

up: build
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

clean:
	$(COMPOSE) down --rmi local --volumes --remove-orphans
	docker builder prune -f

start:
	$(COMPOSE) start

stop:
	$(COMPOSE) stop
