# Telegram Bot for EGE Informatics Preparation

This is a Telegram bot designed to help students prepare for the Russian EGE (Unified State Exam) in Informatics. The bot provides practice tasks, tracks user progress, and offers a simple interface for interactive learning.

## Repository Structure

```
tg_bot_tutor/
│
├── main.py                     # Main bot script
├── .env                        # Environment variables (not tracked)
├── .env.example                # Example environment variables file
├── requirements.txt            # Python dependencies
├── LICENSE                     # License file
├── README.md                   # This file
├── .gitignore                  # Git ignore file
│
├── data/
│   └── tasks.json              # Static database of tasks
│
├── storage/
│   └── user_progress.json      # User progress data (auto-generated on first run)
│
├── handlers/
│   ├── __init__.py
│   └── user_handlers.py        # User interaction logic
│
└── utils/
    ├── __init__.py
    ├── data_loader.py          # Task loading logic
    └── progress_manager.py     # User progress management logic
```

## Features

- Provides practice tasks for EGE Informatics preparation.
- Tracks user progress and saves it to `user_progress.json`.
- Supports multiple task types stored in `tasks.json`.
- Easy-to-use Telegram bot interface.

## Prerequisites

- Python 3.8 or higher
- A Telegram bot token (obtained from [BotFather](https://t.me/BotFather))
- Installed dependencies from `requirements.txt`

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```

4. **Prepare the task database**:
   - Ensure `data/tasks.json` is correctly formatted. An example structure is provided below:
     ```json
     {
       "1": [
         {
           "question": "Задание 1. Найдите значение выражения: 3**4",
           "answers": ["81", "81.0"]
         },
         {
           "question": "Задание 1. Переведите число 110101 из двоичной системы в десятичную.",
           "answers": ["53", "53.0"]
         },
         {
           "question": "Задание 1. Сколько бит в 2 килобайтах (в двоичном понимании)?",
           "answers": ["16384", "16384.0"]
         }
       ],
       "2": [
         {
           "question": "Задание 2. Сколько байт в 32-битном слове?",
           "answers": ["4", "4.0"]
         },
         {
           "question": "Задание 2. Какое минимальное основание может иметь система счисления?",
           "answers": ["2", "2.0"]
         },
         {
           "question": "Задание 2. Переведите число 255 из десятичной системы в шестнадцатеричную.",
           "answers": ["FF"]
         }
       ]
     }
     ```

5. **Run the bot**:
   ```bash
   python main.py
   ```

## Saving Progress

- User progress is automatically saved to `storage/user_progress.json` upon interaction with the bot.
- The file is created automatically on the first run if it doesn't exist.
- Ensure the `storage/` directory has write permissions.

## .env.example

The `.env.example` file provides a template for environment variables. It should look like this:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

Replace `your_bot_token_here` with your actual Telegram bot token in the `.env` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# Telegram-бот для подготовки к ЕГЭ по информатике

Это Telegram-бот, предназначенный для помощи учащимся в подготовке к ЕГЭ по информатике в России. Бот предоставляет практические задания, отслеживает прогресс пользователей и предлагает простой интерфейс для интерактивного обучения.

## Структура репозитория

```
tg_bot_tutor - оператор/
│
├── main.py # Основной скрипт бота
├── .env # Переменные среды (не отслеживаются)
├── .env.example # Пример файла переменных среды
├── requirements.txt # Зависимости Python
├── ЛИЦЕНЗИЯ # Файл лицензии
├── README.md # Этот файл
├── .gitignore # Файл игнорирования Git
│
├── данные/
│ └── задачи.json # Статическая база данных задач
│
├── хранение/
│ └── user_progress.json # Данные о прогрессе пользователя (автоматически генерируются при первом запуске)
│
├── обработчики/
│ ├── __init__.py
│ └── user_handlers.py # Логика взаимодействия с пользователем
│
└── утилиты/
    ├── __init__.py
    ├── data_loader.py # Логика загрузки задач
    └── progress_manager.py # Логика управления прогрессом пользователя
```

## Особенности

- Предоставляет практические задания для подготовки к ЕГЭ по информатике.
- Отслеживает прогресс пользователя и сохраняет его в "user_progress.json".
- Поддерживает несколько типов задач, хранящихся в `tasks.json`.
- Простой в использовании интерфейс Telegram-бота.

## Предварительные условия

- Python 3.8 или выше
- Токен Telegram-бота (полученный от [BotFather](https://t.me/BotFather))
- Установленные зависимости из `requirements.txt`

## Setup

1. **Клонировать репозиторий**:
   ```
клонировать bash git https://github.com/yourusername/your-repo.git
   создать свой репозиторий
   ```

2. **Установите зависимости**:
   ```bash
   установка pip -r requirements.txt
   ```

3. **Настройте переменные окружения**:
   - Скопируйте `.env.example` в `.env`:
     ```bash
cp .env.example .env
     ```

4. **Подготовьте базу данных задач**:
   - Убедитесь, что файл `data/tasks.json` правильно отформатирован. Ниже приведен пример структуры:
     ```json
     {
       "1": [
         {
           "вопрос": "Назначение 1. Найдите значение выражения: 3**4",
            "ответы": ["81", "81.0"]
         },
         {
           "вопрос": "Задание 1. Перевести слово 110101 из двойной системы в повседневную".,
           "ответы": ["53", "53.0"]
         },
         {
           "вопрос": "Задание 1. Как бороться со 2-мя килобайтами (в двойном понимании)?",
           "ответы": ["16384", "16384.0"]
         }
       ],
       "2": [
         {
           "вопрос": "Задание 2. Как вы относитесь к 32-битному слову?",
            "ответы": ["4", "4.0"]
         },
         {
           "вопрос": "Задание 2. Как минимальное понимание может отразиться на системе счисления?",
            "ответы": ["2", "2.0"]
         },
         {
           "вопрос": "Задание 2. Всего было 255 из ежедневной системы мониторинга",
            "ответы": ["FF"]
         }
       ]
     }
     ```

5. **Запустите бота**:
   ```bash
python main.py
   ``

## Сохранение прогресса

- Прогресс пользователя автоматически сохраняется в "хранилище/user_progress.json` при взаимодействии с ботом.
- Файл создается автоматически при первом запуске, если он не существует.
- Убедитесь, что в каталоге `storage/` есть разрешения на запись.

## .env.example

Файл `.env.example` предоставляет шаблон для переменных среды. Он должен выглядеть следующим образом:
```
TELEGRAM_BOT_TOKEN=ваш_бот_токен_ здесь
```

Замените "your_bot_token_here" на ваш реальный токен Telegram-бота в файле ".env".

## Лицензия

Этот проект лицензирован по лицензии MIT. Подробности смотрите в файле [ЛИЦЕНЗИЯ](LICENSE).