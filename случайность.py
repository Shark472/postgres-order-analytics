import random


# 1. Функция-симулятор: генерирует замеры и пишет их в файл
def run_laboratory_experiment(real_value, num_tests, file_path):
    measurements = []

    for _ in range(num_tests):
        # Генерируем случайную погрешность прибора от -0.05 до +0.05 мм
        device_error = random.uniform(-0.05, 0.05)
        # Получаем итоговый замер прибора
        current_measurement = real_value + device_error
        # Округляем до 3 знаков (как на реальном микрометре)
        measurements.append(round(current_measurement, 3))

    # Записываем полученные замеры в файл data.txt через пробел
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(" ".join(map(str, measurements)))

    print(f"🔬 Симуляция успешно завершена!")
    print(f"Создано замеров: {num_tests} шт. Данные сохранены в '{file_path}'\n")


# 2. Твои рабочие метрологические функции
def find_average(data_list):
    return sum(data_list) / len(data_list)


def find_absolute_errors(data_list):
    avg_value = find_average(data_list)
    errors_list = []
    for measurement in data_list:
        error = abs(measurement - avg_value)
        errors_list.append(round(error, 4))
    return errors_list


def find_relative_errors(abs_errors, avg_value):
    relative_list = []
    for error in abs_errors:
        rel_error = (error / avg_value) * 100
        relative_list.append(round(rel_error, 2))
    return relative_list


def load_measurements(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().strip()
        raw_list = content.split()
        return [float(item) for item in raw_list]


# === ТОЧКА ЗАПУСКА ВСЕЙ ПРОГРАММЫ ===
FILE_NAME = "data.txt"
TRUE_SIZE = 10.0  # Истинный размер детали в мм
TOTAL_MEASUREMENTS = 7  # Сколько раз "измеряем" инструмент

# Шаг A: Запускаем симулятор (создаем файл с виртуальными замерами)
run_laboratory_experiment(TRUE_SIZE, TOTAL_MEASUREMENTS, FILE_NAME)

# Шаг Б: Наш калькулятор считывает этот файл и делает расчеты
try:
    my_measurements = load_measurements(FILE_NAME)

    avg = round(find_average(my_measurements), 4)
    abs_errors = find_absolute_errors(my_measurements)
    rel_errors = find_relative_errors(abs_errors, avg)

    # Красивый вывод результатов для отчета
    print("📋 ОТЧЕТ ПО ЛАБОРАТОРНОЙ РАБОТЕ:")
    print("-" * 40)
    print(f"Полученные замеры: {my_measurements}")
    print(f"Среднее значение:  {avg} мм")
    print(f"Абсолютные ошибки: {abs_errors}")
    print(f"Относительные (%):  {rel_errors}")
    print("-" * 40)

except FileNotFoundError:
    print("Ошибка при чтении файла!")
