inventory = ["меч", "щит"]
MAX_CAPACITY = 5  # Создаем переменную максимальной вместимости

print("🎒 Добро пожаловать в менеджер инвентаря!")

while True:
    total_items = len(inventory)
    # Показываем игроку лимит, например: (2/5 предметов)
    print(f"\nСейчас в рюкзаке ({total_items}/{MAX_CAPACITY} предметов): {inventory}")

    print("1 — Добавить предмет")
    print("2 — Выбросить предмет")
    print("3 — Выйти из игры")

    action = input("Выбери действие (1, 2 или 3): ")

    if action == "1":
        # ШАГ 1: Перед добавлением проверяем, есть ли свободное место
        if len(inventory) >= MAX_CAPACITY:
            print("❌ Твой рюкзак переполнен! Выброси что-нибудь сначала.")
        else:
            # ШАГ 2: Если место есть, разрешаем ввод и добавление
            item = input("Какой предмет добавить? ")
            clean_item = item.lower()
            inventory.append(clean_item)
            print(f"✨ {clean_item} добавлен в рюкзак!")

    elif action == "2":
        item = input("Какой предмет выбросить? ")
        clean_item = item.lower()

        if clean_item in inventory:
            inventory.remove(clean_item)
            print(f"🗑 Ты выбросил {clean_item}!")
        else:
            print(f"❌ Ошибка! Предмета '{clean_item}' нет в рюкзаке.")

    elif action == "3":
        print("🎒 Игра сохранена. До встречи!")
        break
    else:
        print("🤔 Неизвестная команда, попробуй еще раз.")

