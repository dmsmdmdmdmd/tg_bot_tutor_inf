import json
import os

PROGRESS_FILE = os.path.join(os.path.dirname(__file__), '..', 'storage', 'user_progress.json')
PROGRESS_FILE = os.path.abspath(PROGRESS_FILE)

def _load_progress():
    """Загружает JSON-файл с прогрессом пользователей"""
    if not os.path.exists(PROGRESS_FILE):
        return {}
    try:
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def _save_progress(data):
    """Сохраняет прогресс пользователей в файл"""
    os.makedirs(os.path.dirname(PROGRESS_FILE), exist_ok=True)
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_solved_task(user_id: int, task_number: str):
    """Добавляет +1 к количеству решённых заданий данного типа"""
    data = _load_progress()
    user_id = str(user_id)
    if user_id not in data:
        data[user_id] = {}
    if task_number not in data[user_id]:
        data[user_id][task_number] = 0
    data[user_id][task_number] += 1
    _save_progress(data)

def get_user_stats(user_id: int):
    """Возвращает словарь с прогрессом пользователя"""
    data = _load_progress()
    return data.get(str(user_id), {})

def get_total_solved(user_id: int):
    """Считает общее количество решённых задач"""
    stats = get_user_stats(user_id)
    return sum(stats.values())