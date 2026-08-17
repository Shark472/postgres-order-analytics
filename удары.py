import random


# 1. Функция расчета урона ИГРОКА (возвращает число)
def calculate_player_damage(base_damage):
    crit = random.randint(1, 15)
    return base_damage + crit


# 2. Функция расчета урона ПРИЗРАКА (возвращает число)
def calculate_enemy_damage():
    # Призраки бьют больно, от 10 до 25 урона
    return random.randint(10, 25)


print("=== ДОБРО ПОЖАЛОВАТЬ В РУИНЫ НОВОГО ЛОНДО ===")

# Характеристики бойцов
player_hp = 100
ghost_hp = 120

print("Перед тобой вырос жуткий Призрак Нового Лондо!")
print("Выбери оружие на этот бой:")
print("1 — Меч Дракона (Базовый урон: 30)")
print("2 — Секира Рыцаря (Базовый урон: 45)")

weapon_choice = input("Твой выбор (1 или 2): ").strip()

# Записываем характеристики выбранного оружия
if weapon_choice == "2":
    weapon_name = "Секира Рыцаря"
    weapon_base = 45
else:
    # Если ввел 1 или что-то другое, по дефолту даем Меч
    weapon_name = "Меч Дракона"
    weapon_base = 30

print(f"\n⚔️ Ты крепко сжал [{weapon_name}]. Бой начался! ⚔️")

# 3. Главный цикл боя — пока оба живы
while player_hp > 0 and ghost_hp > 0:
    print(f"\n❤ Твое здоровье: {player_hp} HP | 👻 Здоровье Призрака: {ghost_hp} HP")
    action = input("Нажми Enter, чтобы атаковать (или напиши 'бежать'): ").strip().lower()

    if action == "бежать":
        print("🏃‍♂️ Ты в панике сбежал к Храму Огня!")
        break

    # --- ХОД ИГРОКА ---
    player_damage = calculate_player_damage(weapon_base)
    ghost_hp = ghost_hp - player_damage
    print(f"💥 Ты ударил [{weapon_name}] и нанес {player_damage} урона!")

    # Проверяем, не умер ли призрак от нашего удара
    if ghost_hp <= 0:
        ghost_hp = 0
        print("\n🎉 ПОБЕДА! Призрак растворился в воздухе. Ты выжил!")
        break  # Выходим из цикла, игра окончена

    # --- ХОД ПРИЗРАКА ---
    print("👻 Призрак пролетает сквозь стену и контратакует!")
    ghost_damage = calculate_enemy_damage()
    player_hp = player_hp - ghost_damage
    print(f"🩸 Жуткие когти призрака нанесли тебе {ghost_damage} урона!")

    # Проверяем, не умер ли игрок
    if player_hp <= 0:
        player_hp = 0
        print("\n💀 ВЫ УМЕРЛИ. Призрак забрал твою душу... Возвращение у костра.")
        break

print("\n=== Бой завершен ===")
