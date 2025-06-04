# URL-alias-service

Сервис сокращения ссылок на Django + PostgreSQL

## Установка

1. Клонируем репозиторий

```bash
git clone git@github.com:Searchforsomething/url-alias-service.git
```

2. Переходим в корень проекта

```bash
cd url-alias-service
```

3. Выполняем команду для сборки

```bash
sudo docker compose up --build
```

Для создания пользователя необходимо выполнить:

```bash
sudo docker compose exec api python manage.py createsuperuser
```

## API Эндпоинты

### Приватные эндпоинты:

`POST /api/create/` - создание короткой ссылки

`POST /api/deactivate/<str:short_id>/` - деактивация ссылки по её короткому id  

`GET /api/list/` - получение списка созданных ссылок  

`GET /api/stats/` - получение статистики переходов по ссылкам

### Публичный эндпоинт:

`GET /<str:short_id>/` - переход по ссылке

### Swagger

Подробнее информацию об эндпойнтах можно посмотреть в swagger по пути `/docs/`

### Авторизация

Авторизоваться можно перейдя по пути `/admin/`

## Ограничения и недостатки

1. Сервер с апи запускается в режиме дебага, что делает работу с ним легче,
но в то же время ухудшает его безопасность
2. Нет тестов