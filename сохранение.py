def load_game():
    with open("data.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()  # Прочитали все строки в список

    # Разбираем имя (индекс 0)
    name_line = lines[0].strip()
    name = name_line.split(": ")[1]

    # Разбираем здоровье (индекс 1)
    hp_line = lines[1].strip()
    hp = int(hp_line.split(": ")[1])

    # Разбираем золото (индекс 2)
    gold_line = lines[2].strip()
    gold = int(gold_line.split(": ")[1])

    # Выталкиваем все три переменные наружу в игру
    return name, hp, gold


# А вот так мы вызываем эту функцию в самой игре:
player_name, player_hp, player_gold = load_game()

print(f"Добро пожаловать обратно, {player_name}!")
print(f"Твоё здоровье: {player_hp}, золото в кармане: {player_gold}")

