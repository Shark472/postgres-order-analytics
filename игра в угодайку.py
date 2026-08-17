import random

secret_number = random.randint(1, 20)  # Снизим диапазон до 20, так как попыток мало
lives = 5  # Количество твоих жизней

print("🤖 Я загадал число от 1 до 20. У тебя есть всего 5 жизней, чтобы угадать его!")

# Цикл работает, ПОКА количество жизней больше нуля
while lives > 0:
    print(f"❤️ Осталось жизней: {lives}")
    user_guess = input("Введи число: ")
    guess_number = int(user_guess)

    if guess_number == secret_number:
        print(f"🎉 Невероятно! Ты победил! Это было число {secret_number}!")
        break
    elif guess_number < secret_number:
        print("Моё число БОЛЬШЕ.")
    else:
        print("Моё число МЕНЬШЕ.")

    lives = lives - 1  # Забираем одну жизнь за неверный ответ
    print("-" * 20)  # Просто черта для красоты между попытками

# Этот кусок сработает, только если цикл закончился, а break не случился
if lives == 0:
    print(f"💀 Жизни закончились! Ты проиграл. Компьютер загадал число {secret_number}.")
