from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from utils.data_loader import load_tasks
from utils.progress_manager import add_solved_task, get_user_stats

router = Router()
tasks = load_tasks()

# Состояние пользователей (в памяти)
user_state = {}

# ---------- Клавиатуры ----------

def get_navigation_keyboard():
    kb = [
        [KeyboardButton(text="←"), KeyboardButton(text="→")],
        [KeyboardButton(text="Отмена")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def get_continue_keyboard():
    kb = [
        [KeyboardButton(text="Продолжить"), KeyboardButton(text="Сменить тип")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# ---------- Вспомогательные функции ----------

def normalize_answer(ans: str):
    """Приводит ответ к единому виду (18 == 18.0)"""
    ans = ans.strip().lower().replace(',', '.')
    try:
        return str(float(ans))
    except ValueError:
        return ans

# ---------- Команды ----------

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот для подготовки к ЕГЭ по информатике.\n\n"
        "Напиши номер задания от 1 до 27, и я пришлю тебе задачу для тренировки.",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer(
        "📘 Введи число от 1 до 27 — это номер задания ЕГЭ.\n"
        "После этого ты сможешь:\n"
        "➡️ Листать задачи стрелками\n"
        "💬 Отправить свой ответ\n"
        "❌ Нажать 'Отмена', чтобы вернуться к выбору задания.",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(Command("stats"))
async def stats_cmd(message: types.Message):
    stats = get_user_stats(message.from_user.id)
    if not stats:
        await message.answer("📊 У тебя пока нет решённых заданий.")
        return

    total = sum(stats.values())
    text = "📈 Твой прогресс:\n\n"
    for k, v in sorted(stats.items(), key=lambda x: int(x[0])):
        text += f"Задание {k}: {v} ✅\n"
    text += f"\nВсего решено: {total} задач 💪"
    await message.answer(text)

# ---------- Основная логика ----------

@router.message(F.text.in_([str(i) for i in range(1, 28)]))
async def select_task(message: types.Message):
    user_id = message.from_user.id
    text = message.text.strip()

    # Если пользователь решает задание — это не выбор нового задания, а попытка ответа
    if user_id in user_state and "task_number" in user_state[user_id]:
        await check_answer(message)
        return

    if text not in tasks:
        await message.answer("Такого задания пока нет 😔")
        return

    user_state[user_id] = {"task_number": text, "index": 0}
    question = tasks[text][0]["question"]

    await message.answer(f"📘 {question}", reply_markup=get_navigation_keyboard())

@router.message(F.text == "→")
async def next_task(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_state:
        await message.answer("Сначала выбери номер задания (1–27).")
        return

    state = user_state[user_id]
    task_number = state["task_number"]
    state["index"] = (state["index"] + 1) % len(tasks[task_number])
    question = tasks[task_number][state["index"]]["question"]

    await message.answer(f"📘 {question}", reply_markup=get_navigation_keyboard())

@router.message(F.text == "←")
async def prev_task(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_state:
        await message.answer("Сначала выбери номер задания (1–27).")
        return

    state = user_state[user_id]
    task_number = state["task_number"]
    state["index"] = (state["index"] - 1) % len(tasks[task_number])
    question = tasks[task_number][state["index"]]["question"]

    await message.answer(f"📘 {question}", reply_markup=get_navigation_keyboard())

@router.message(F.text == "Отмена")
async def cancel_task(message: types.Message):
    user_state.pop(message.from_user.id, None)
    await message.answer("Выбери новое задание от 1 до 27:", reply_markup=ReplyKeyboardRemove())

@router.message(F.text.in_(["Продолжить", "Сменить тип"]))
async def continue_or_change(message: types.Message):
    user_id = message.from_user.id

    if message.text == "Продолжить":
        state = user_state.get(user_id)
        if not state:
            await message.answer("Сначала выбери задание.")
            return
        task_number = state["task_number"]
        question = tasks[task_number][state["index"]]["question"]
        await message.answer(f"📘 {question}", reply_markup=get_navigation_keyboard())
    else:
        user_state.pop(user_id, None)
        await message.answer("Введите номер нового задания (1–27):", reply_markup=ReplyKeyboardRemove())

@router.message()
async def check_answer(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_state:
        await message.answer("Напиши номер задания от 1 до 27, чтобы начать.")
        return

    state = user_state[user_id]
    task_number = state["task_number"]
    index = state["index"]
    correct_answers = [normalize_answer(a) for a in tasks[task_number][index]["answers"]]
    user_answer = normalize_answer(message.text)

    if user_answer in correct_answers:
        await message.answer("✅ Отлично! Всё верно!", reply_markup=get_continue_keyboard())
        add_solved_task(user_id, task_number)
    else:
        await message.answer("❌ Неправильно. Попробуй ещё раз 🤔", reply_markup=get_navigation_keyboard())