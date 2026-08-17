# Наш рюкзак с вещами
inventory = ["ржавый клинок", "секира рыцаря", "посох мага"]
# Переменная для оружия, которое сейчас в руках (изначально пусто)
equipped_weapon = "Ничего"

print("⚔️ Добро пожаловать в оружейную Dark Souls!")

while True:
    print("\n" + "=" * 40)
    print(f"Сейчас в руках: 👉 {equipped_weapon} 👈")
    print("Содержимое рюкзака:")

    # 1. Выводим рюкзак в красивом нумерованном виде через цикл for
    for index, item in enumerate(inventory):
        print(f"  [{index + 1}] — {item}")

    print("\nДоступные действия:")
    print("  [номер] — Введи цифру предмета, чтобы взять его в руки")
    print("  [выход] — Закрыть меню оружия")
    print("=" * 40)

    user_input = input("Твой выбор: ").strip().lower()

    # Проверяем команду выхода
    if user_input == "выход":
        print("Вы вышли из меню экипировки. В бой!")
        break

    # 2. Проверяем, ввёл ли пользователь число
    elif user_input.isdigit():
        # Переводим текст в число и вычитаем 1, чтобы вернуть правильный индекс Python (0, 1, 2)
        choice_index = int(user_input) - 1

        # Защита от дурака: проверяем, существует ли предмет под таким номером в списке
        if 0 <= choice_index < len(inventory):
            # Берем выбранный предмет из списка
            selected_item = inventory[choice_index]

            # Логика рокировки:
            if equipped_weapon != "Ничего":
                # Если в руках уже что-то было, возвращаем это обратно в рюкзак
                inventory.append(equipped_weapon)

            # Кладем новое оружие в руки
            equipped_weapon = selected_item
            # Удаляем его из рюкзака, ведь оно теперь в руках!
            inventory.remove(selected_item)

            print(f"✨ Ты экипировал: {equipped_weapon}!")
        else:
            print("❌ Ошибка! Предмета с таким номером нет в рюкзаке.")
    else:
        print("🤔 Неверный ввод. Введи номер предмета или слово 'выход'.")
