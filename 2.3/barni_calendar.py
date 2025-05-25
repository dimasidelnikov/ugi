from ics import Calendar, Event
from datetime import datetime

# Список событий
events = [
    ("Бровекта", "2024-11-13"),
    ("От глистов", "2024-11-22"),
    ("Бровекта", "2025-02-08"),
    ("От глистов", "2025-02-10"),
    ("Бровекта и от глистов", "2025-05-10"),
    ("От аллергии", "2025-05-10"),
    ("Бровекта", "2025-09-10"),
    ("От глистов", "2025-11-10"),
    ("От аллергии", "2025-09-10"),
    ("Бровекта и от глистов и от аллергии", "2026-02-10")
]

# Создаем календарь
calendar = Calendar()

for title, date_str in events:
    event = Event()
    event.name = f"Барни: {title}"
    event.begin = datetime.strptime(date_str, "%Y-%m-%d").date()
    calendar.events.add(event)

# Сохраняем в файл
with open("График_таблеток_Барни.ics", "w", encoding="utf-8") as f:
    f.writelines(calendar)

print("Файл График_таблеток_Барни.ics успешно создан!")
