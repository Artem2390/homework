class TrainerNotFoundError(Exception):
    def __init__(self, message="Тренер не знайдений"):
        self.message = message
        super().__init__(self.message)


sports = {
    1: "Футбол",
    2: "Баскетбол",
    3: "Теніс",
}

coaches = {
    "Петров": "Футбол",
    "Іванов": "Баскетбол",
    "Сидоров": "Теніс",
}

schedule = {
    "Понеділок": "Футбол - 10:00, Баскетбол - 14:00",
    "Вівторок": "Теніс - 11:00, Футбол - 15:00",
    "Середа": "Баскетбол - 9:00, Теніс - 13:00",
}

cost = {
    "Футбол": 200,
    "Баскетбол": 150,
    "Теніс": 100,
}

while True:
    print("\nМеню:")
    print("1 - Перелік видів спорту")
    print("2 - Команда тренерів")
    print("3 - Розклад тренувань")
    print("4 - Вартість тренування")
    print("5 - Пошук тренера за прізвищем")
    print("6 - Вихід")

    choice = input("Оберіть пункт меню: ")

    if choice == '1':
        print("Перелік видів спорту:")
        for key, value in sports.items():
            print(f"{key}: {value}")

    elif choice == '2':
        print("Команда тренерів:")
        for coach, sport in coaches.items():
            print(f"{coach} - {sport}")

    elif choice == '3':
        print("Розклад тренувань:")
        for day, training in schedule.items():
            print(f"{day}: {training}")

    elif choice == '4':
        print("Вартість тренування:")
        for sport, price in cost.items():
            print(f"{sport}: {price} грн")

    elif choice == '5':
        last_name = input("Введіть прізвище тренера: ")
        try:
            sport = coaches[last_name]
            print(f"Тренер {last_name} працює з командою з {sport}")
        except KeyError:
            raise TrainerNotFoundError()

    elif choice == '6':
        print("Програма завершена.")
        break

    else:
        print("Некоректний вибір. Спробуйте ще раз.")
