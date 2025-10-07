import json
import os

def load_tasks():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'tasks.json')
    data_path = os.path.abspath(data_path)
    
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] Файл tasks.json не найден по пути: {data_path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"[ERROR] Ошибка в JSON файле: {e}")
        return {}