### Hexlet tests and linter status:
[![Actions Status](https://github.com/NeishchenkoAlex/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/NeishchenkoAlex/python-project-50/actions)   [![Maintainability](https://api.codeclimate.com/v1/badges/0f65beb26ed228d1329f/maintainability)](https://codeclimate.com/github/NeishchenkoAlex/python-project-50/maintainability)    [![Test Coverage](https://api.codeclimate.com/v1/badges/0f65beb26ed228d1329f/test_coverage)](https://codeclimate.com/github/NeishchenkoAlex/python-project-50/test_coverage)
###          Утилита для сравнения файлов формата(JSON/YAML)

> #### - Описание утилиты:

 производит сравнение файлов в форматах JSON и YAML. Программа анализирует различия между двумя файлами и выводит результат.

>#### - Параметры утилиты:

 - сравнивает 2 файла в формате JSON/YAML
 - имеет 3 формата вывода результата
 - результат определяет добавление,удаление и изменение значений

>#### - Установка утилиты:

Откройте терминал:

1. Выполните клонирование репозитория командой:

> git clone https://github.com/NeishchenkoAlex/python-project-50.git

2. Перейдите в директорию проекта:

> cd python-project-50

3. Установите зависимости:

> make install

4. Установите пакет с утилитой:

> make build

после установки можно приступить к использованию.

>#### - Примеры использования утилиты:

Основная команда:

> gendiff tests/fixtures/file3.json tests/fixtures/file4.json

[![asciicast](https://asciinema.org/a/LvIy5Mlft2wwEPBy71LKZIYsb.svg)](https://asciinema.org/a/LvIy5Mlft2wwEPBy71LKZIYsb)

Опции:

> gendiff -h

[![asciicast](https://asciinema.org/a/JMdMVfsfXYDgq9XNQKg4MxItp.svg)](https://asciinema.org/a/JMdMVfsfXYDgq9XNQKg4MxItp)

Форматы вывода:

> - Программа поддерживает несколько форматов вывода:

> - stylish (по умолчанию) — древовидный формат

> - plain — текстовое описание изменений

> - json — формат JSON

Формат plain:

> gendiff -f plain tests/fixtures/file3.json tests/fixtures/file4.json

[![asciicast](https://asciinema.org/a/SoHQJyEHWumYlHuIby9U6lH3c.svg)](https://asciinema.org/a/SoHQJyEHWumYlHuIby9U6lH3c)

Формат json:

> gendiff -f json tests/fixtures/file3.json tests/fixtures/file4.json

[![asciicast](https://asciinema.org/a/Qtmtk0o9LRPG0mlI981Sd9sQx.svg)](https://asciinema.org/a/Qtmtk0o9LRPG0mlI981Sd9sQx)

>#### - Тестирование утилиты:

выполните команду в терминале:

> make test-coverage






