# Makefile для управления Docker Compose

.PHONY: build up test down down-v

# Сборка сервисов
build:
	docker compose build

# Запуск сервисов db, redis, api в фоне
up:
	docker compose up -d db redis api

# Запуск тестов (api-test) с автоматическим удалением контейнера после выполнения
test:
	docker compose run --rm api-test

# Остановка сервисов
down:
	docker compose down

# Остановка сервисов с удалением volumes
down-v:
	docker compose down -v
