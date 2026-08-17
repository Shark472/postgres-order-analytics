print("=== Вечный Python-калькулятор ===")

while True:
    # Спрашиваем у пользователя числа
    num1 = float(input("Введи первое число: "))
    num2 = float(input("Введи второе число: "))
    operation = input("Выбери операцию (+, -, *, /): ")

    # Считаем результат
    if operation == "+":
        print(f"Результат: {num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"Результат: {num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        print(f"Результат: {num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        if num2 == 0:
            print("Ошибка! На ноль делить нельзя.")
        else:
            print(f"Результат: {num1} / {num2} = {num1 / num2}")
    else:
        print("Ошибка! Неверный знак операции.")

    print("-" * 30)  # Разделитель для красоты

    # Спрашиваем, нужно ли продолжать
    answer = input("Хочешь посчитать что-то еще? (да/нет): ")
    if answer.lower() == "нет" or answer.lower() == "н":
        print("Спасибо за использование калькулятора! До свидания!")
        break  # Останавливаем цикл и выходим

    print("=" * 30)  # Разделитель перед новым кругом

