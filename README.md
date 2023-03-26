# Тестовое задание для направления "Python development"

Здесь представлен компактный веб-сервис, позволяющий работать с авторами и книгами.

Проект представляет собой сайт, предназначеный для просмотра, добавления писателей и их книг.

Запуск и тестирование сайта
===========================
Для запуска сайта на компьютере необходимы следующие программы:
python = "3.10"
poetry = "1.3.2"

Первый запуск
-------------
Для начала работы Вам необходимо клонировать репозиторий с сайтом на свой компьютер. 
Запустите консоль и перейдите в корневую папку репозитория.
Загрузите необходимые библиотеки в виртуальное окружение командной 'poetry install'.
Автоматически будут загружены все необходимые библиотеки, в том числе "django v4.17".
Для запуска тестов перейдите в папку 'project' корневого каталога и введите в консоль команду "poetry run python manage.py test library".
При успешном завершении тестов в консоли должен быть показан статус "ОК". В противном случае обратитесь по адресу электронной почты, указанной ниже.
Для запуска сайта, в той же папке 'project', введите в консоль команду "poetry run python manage.py runserver".
При успешном запуске сайта в консоли будет указан URL для активного сайта, с которым вы уже можете начать работу.

О сайте
-------
Интерфейс сделан интуитивно понятным. Для добавления новых книг/авторов необходимо войти/зарегистрироваться.
Для доступа к админ панели, 'path' URL-а укажите как '/admin/'.
В базе данных уже есть созданный тестовый аккаунт с правами суперюзера(login - "admin", password - "admin").
Так же в базе данных уже есть несколько книг и авторов, для возможности немедленно проверит функционал.

Для разработчиков
=================
Тестирование сайта представлено unit-тестами.
CI/CD панчлайн реализован с "GitGub action".
При попытке совершить Push/PullRequest на репозиторий в GitHub, будут автоматически проведены unit-тесты.
На данном этапе весь панчлайн состоит из двух последовательно выполняемых тестов.

Обратная связь
==============
По вопросам, связанным с сайтом, обращатесь по адресу электронной почты "785vvv@gmail.com'

