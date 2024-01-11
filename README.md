# Задание для Backend-стажировки на Python и Django

Создайте веб-приложение на Django, которое будет реализовывать функциональность библиотеки книг.

## Содержание

- [Основные требования](#Основные-требования)
  - [Модели](#Модели)
  - [Функционал](#Функционал)
  - [API](#API)
  - [Дополнительные задачи](#Дополнительные-задачи)
  - [Требования к коду](#Требования-к-коду)
- [Реализация](#Реализация)
  - [Основное приложение books_app](#Основное-приложение-books_app)
  - [Приложение пользователей user_app](#Приложение-пользователей-user_app)
  - [Приложение для API api_app](#Приложение-для-API-api_app)
- [Демо](#Демо)
- [Запуск](#Запуск)
  - [Запуск проекта](#Запуск-проекта-локально)
  - [Запуск проекта в Docker-контейнере](#Запуск-проекта-в-Docker-контейнере)
- [Автор](#Автор)

## Основные требования

### Модели:
- Книга (название, автор, год издания, краткое описание, изображение обложки)
- Автор (имя, дата рождения, краткая биография)
- Пользователь (стандартная модель пользователя Django с расширенными полями, если необходимо)

### Функционал:
- Регистрация/Авторизация пользователей
- Просмотр списка книг
- Просмотр детальной информации о книге
- Поиск книг по названию или автору
- Возможность добавлять, редактировать и удалять книги (только для администраторов или авторизованных пользователей)
- Возможность оставлять комментарии к книгам (для авторизованных пользователей)

### API:
- Реализовать API endpoints для просмотра списка книг и детальной информации о книге. Используйте Django Rest Framework.

### Дополнительные задачи:
- Реализация пагинации для списка книг
- Возможность рейтинга книг пользователем
- Использование Docker для развертывания приложения
- Автоматические тесты для основного функционала

### Требования к коду:
- Код должен быть написан аккуратно и следовать PEP 8.
- Комментарии к сложным или неочевидным местам.
- Четкое разделение логики между views, models и templates.

## Реализация

### Основное приложение books_app:

- Создана модель Автора и Книги. Дополнительно создана модель Комментарии
- Модели зарегистрированы в админке.
- Создано 8 представлений. Все представления на основе классов:
  - Страница со всеми книгами
  - Страница книги
  - Страница изменения комментария - кнопка видна только автору комментария
  - Страница подтверждения удаления комментария - кнопка видна только автору комментария
  - Страница добавления книги - доступна только суперпользователю или пользователю из группы `editors`
  - Страница изменения книги - доступна только суперпользователю или пользователю из группы `editors`
  - Страница удаления книги - доступна только суперпользователю или пользователю из группы `editors`
  - Страница с результатами поиска
- Созданы 5 форм. Вместо использования стандартных в представлениях, в основном для назначения имени полю, указания ограничений и добавления Bootstrap-классов.
- Создан и зарегистрирован контекстный процессор, передающий на все страницы форму поиска.
- Реализована возможность оценить книгу зарегистрированному пользователю

### Приложение пользователей user_app:
- Переопределены формы регистрации и авторизации для добавления Bootstrap-классов
- Написаны два представления

### Приложение для API api_app:
- Написан сериализатор для модели книг
- Созданы два представления для получения GET-запросов.

## Демо

Проект запущен на VPS-сервере в Docker-контейнере.
Сайт доступен по ссылке: ~~удалён~~

API:  
Все книги - метод GET: `/api/all_books/`
Книга - метод GET: `/api/get_book/<int:pk>`

## Запуск

Логин и пароль суперпользователя: `admin`

### Запуск проекта локально:
```bash
# 1. Скачать и распаковать репозиторий
# 2. Открыть проект в Pycharm или в виртуальном окружении
# 3. Установить пакеты:
pip install -r requirements.txt
# 4. Запустить проект:
python manage.py runserver
```
### Запуск проекта в Docker-контейнере:

```bash
# 1. Скачать и распаковать репозиторий
# 2. Открыть в терминале директорию проекта
# 3. Выполнить сборку образа:
sudo docker build -t lad_image .
# 4. Запустить контейнер:
sudo docker run --name lad -p 9999:9999 -d lad_image
```

## Автор:
Тестовое задание выполнил [Иван "proDream" Ашихмин](https://github.com/proDreams)
