# style-guide-project

Стайлгайд документации сервиса подготовки к техническим собеседованиям. Учебный проект по лабораторной работе № 3: Docs as Code, MkDocs, линтинг, GitHub Actions и взаимное ревью.

[Сайт руководства](https://wurlinney.github.io/style-guide-project/) · [Проверки и публикации](https://github.com/wurlinney/style-guide-project/actions/workflows/docs.yml)

## Содержание

- Назначение, аудитория и границы учебной модели.
- Язык, терминология, структура и оформление.
- Шаблоны пользовательской инструкции, задания, API и руководства разработчика.
- Ошибки, достоверность, проверка и сопровождение.
- Два примера: запуск тренировки и задача с разбором на Python.

## Быстрый старт

Требуется Python 3.12. Выполните команды из корня репозитория:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs serve
```

На Windows вместо `source` выполните `.venv\Scripts\Activate.ps1` в PowerShell. Откройте адрес, который напечатает MkDocs, обычно `http://127.0.0.1:8000/`. Остановить сервер можно сочетанием Ctrl+C.

## Проверка

В активированном окружении выполните:

```bash
python -m pymarkdown --config .pymarkdown.json scan --recurse README.md CONTRIBUTING.md .github/pull_request_template.md docs
python -m unittest discover -s tests -v
python -m mkdocs build --strict
```

Линтер проверяет Markdown, тесты выполняют код из опубликованного примера, MkDocs проверяет сборку, навигацию и внутренние ссылки. Эти проверки не оценивают достоверность текста и не заменяют ревью.

## Публикация

Workflow `Documentation` проверяет каждый PR в `main`. После push или merge в `main` он повторяет проверки и публикует сайт в GitHub Pages. В настройках репозитория выберите `Settings → Pages → Source → GitHub Actions`. Ручной запуск доступен во вкладке `Actions`; публикация разрешена только из `main`.

Результат сборки находится в `site/` и не хранится в Git. Полный процесс изменений описан в [CONTRIBUTING.md](CONTRIBUTING.md).
