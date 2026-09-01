# MDI Assistant

Учебный Telegram-бот для студентов программы HSE MDI. Через простое меню он собирает в одном месте основную информацию о дисциплинах: преподавателей и контакты, формулу оценки, ссылки на курс, чат и ведомость.

> **Статус:** исторический студенческий прототип с данными за 2022/2023 учебный год. Ссылки, контакты и правила оценивания могут быть неактуальны.

## Возможности

- список дисциплин в Telegram-клавиатуре;
- карточка курса в ответ на выбор пользователя;
- контакты преподавателей;
- формула итоговой оценки;
- ссылки на LMS, чат курса и ведомость;
- команды `/start` и `/Stop`.

## Как пользоваться ботом

1. Найдите `MDIAssist_bot` в Telegram и нажмите **Start**.
2. Отправьте `/disciplines`.
3. Выберите дисциплину на клавиатуре.
4. Получите собранную информацию о курсе.
5. Нажмите `/Stop`, чтобы скрыть клавиатуру.

<p align="center">
  <img src="https://github.com/dianamarz/kartinki/blob/main/IMG_4.jpeg?raw=true" width="360" alt="Выбор дисциплины в MDI Assistant">
  <img src="https://github.com/dianamarz/kartinki/blob/main/IMG_5.jpeg?raw=true" width="280" alt="Карточка дисциплины в MDI Assistant">
</p>

## Технологии

- Python 3;
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI);
- long polling;
- `unittest` для проверки выбора дисциплин.

## Локальный запуск

```bash
git clone https://github.com/gguzhov/MDI_assistant_project.git
cd MDI_assistant_project

python -m venv .venv
source .venv/bin/activate
pip install -r requirements
python MDI_assist.py
```

### Перед запуском

В исторической версии токен Telegram-бота находится в исходном файле. Его нужно считать скомпрометированным: отозвать через BotFather, выпустить новый и загружать его из переменной окружения, а не хранить в Git.

## Тесты

```bash
python -m unittest unit_test.py
```

## Структура

| Файл | Назначение |
| --- | --- |
| `MDI_assist.py` | логика бота и данные дисциплин |
| `unit_test.py` | тесты функции выбора дисциплины |
| `requirements` | Python-зависимости |

## Команда проекта

[Diana Marzaganova](https://github.com/dianamarz) · [Margarita Gasparova](https://github.com/margogs) · [Gennady Guzhov](https://github.com/gguzhov) · [Daniil Babaev](https://github.com/ThrPHP)
