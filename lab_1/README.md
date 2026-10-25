# Лабораторная работа № 1

**Тема:** Git, GitHub Actions и непрерывная интеграция.

## Описание

Программа для обработки оценок студентов и расчёта среднего рейтинга.

Индивидуальное задание (вариант № 1):
- Чтение данных из YAML-файла.
- Подсчёт студентов, имеющих оценки не ниже 90 по всем дисциплинам.

## Используемые технологии

Python, PyYAML, pytest, pycodestyle, GitHub Actions.

## Запуск

Установка зависимостей:

    pip install -r lab_1/requirements.txt

Запуск с YAML:

    python lab_1/src/main.py -p lab_1/data/data.yaml

Запуск с TXT:

    python lab_1/src/main.py -p lab_1/data/data.txt

## Тестирование

    python -m pytest lab_1/test -v

    pycodestyle lab_1/src lab_1/test

Автоматическая проверка выполняется через GitHub Actions.

## UML-диаграмма

См. [диаграмму классов](diagram.md).

## Вывод

Реализованы чтение TXT и YAML, расчёт среднего рейтинга и подсчёт отличников. Написаны модульные тесты и настроена автоматическая проверка проекта через GitHub Actions.
