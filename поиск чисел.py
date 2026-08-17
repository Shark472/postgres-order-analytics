import math
import logging

# Настраиваем запись в файл history.log
logging.basicConfig(
    filename='history.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)

def log_results(avg, sko):
    # Эта функция будет записывать результат в файл
    message = f"Расчет выполнен: Среднее={avg}, СКО={sko}"
    logging.info(message)
    print("Результат сохранен в history.log")


# --- Метрологические функции ---

def find_average(data):
    """Считает среднее арифметическое."""
    return sum(data) / len(data)


def calculate_sko(data, avg):
    """Считает среднее квадратичное отклонение (S)."""
    # Используем формулу для выборки (n-1), как принято в лабах ЧТОТиБ
    sum_sq = sum((x - avg) ** 2 for x in data)
    return math.sqrt(sum_sq / (len(data) - 1))


def run_calculator():
    print("=== ПУТЬ К ЦЕЛИ 1: Метрологический Помощник (Desktop) ===")
    print("Вводи замеры по одному. Чтобы закончить, нажми Enter.")

    measurements = []
    while True:
        raw_input = input("Замер: ").strip()
        if not raw_input:
            break
        try:
            measurements.append(float(raw_input))
        except ValueError:
            print("Ошибка: введи число!")

    if len(measurements) < 2:
        print("Мало данных для анализа (нужно хотя бы 2 замера).")
        return

    # Основные расчеты
    avg = find_average(measurements)
    sko = calculate_sko(measurements, avg)

    # Расчет погрешностей для каждого замера
    abs_errors = [abs(x - avg) for x in measurements]
    rel_errors = [(err / avg) * 100 for err in abs_errors]

    # Красивый вывод таблицы
    print("\n" + "=" * 45)
    print(f"Среднее значение: {avg:.4f} мм")
    print(f"СКО (S):          {sko:.4f} мм")
    print("-" * 45)
    print(f"{'№':<3} | {'Замер':<10} | {'Абс. погр.':<10} | {'Отн. %':<8}")
    print("-" * 45)

    for i, val in enumerate(measurements):
        print(f"{i + 1:<3} | {val:<10.3f} | {abs_errors[i]:<10.4f} | {rel_errors[i]:<8.2f}")
    print("=" * 45)


if __name__ == "__main__":
    run_calculator()
