import psycopg2


def get_db_connection():
    # Настройки подключения (впиши свой пароль)
    return psycopg2.connect(
        user="postgres",
        password="твой_пароль",  # ПОМЕНЯЙ НА СВОЙ ПАРОЛЬ
        host="127.0.0.1",
        port="5432",
        database="postgres",
    )


def add_order():
    name = input("Введите имя клиента: ")
    price = float(input("Введите сумму заказа (руб): "))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (customer_name, price, status) VALUES (%s, %s, 'new');",
        (name, price),
    )
    conn.commit()
    print(f"✔️ Заказ для {name} добавлен!\n")
    cursor.close()
    conn.close()


def show_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Твоя фишка: сортировка по убыванию цены
    cursor.execute(
        "SELECT id, customer_name, price, status FROM orders ORDER BY price DESC;"
    )
    orders = cursor.fetchall()

    print("\n--- Список заказов (от дорогих к дешевым) ---")
    for o in orders:
        print(f"ID: {o[0]} | Клиент: {o[1]} | Сумма: {o[2]} руб. | Статус: {o[3]}")
    print("---------------------------------------------\n")
    cursor.close()
    conn.close()


def show_analytics():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Собираем аналитику через агрегатные функции SQL
    cursor.execute("SELECT SUM(price), AVG(price), COUNT(*) FROM orders;")
    total_sum, avg_price, total_count = cursor.fetchone()

    print("\n--- Финансовая аналитика базы ---")
    print(f"Общая выручка: {total_sum or 0:.2f} руб.")
    print(f"Средний чек: {avg_price or 0:.2f} руб.")
    print(f"Всего заказов в системе: {total_count} шт.")
    print("---------------------------------\n")
    cursor.close()
    conn.close()


def main_menu():
    while True:
        print("1. Добавить новый заказ")
        print("2. Показать все заказы (сортировка по цене)")
        print("3. Посмотреть финансовую аналитику")
        print("4. Выйти")

        choice = input("Выберите действие (1-4): ")

        if choice == "1":
            add_order()
        elif choice == "2":
            show_orders()
        elif choice == "3":
            show_analytics()
        elif choice == "4":
            print("Работа завершена. Тишина и покой.")
            break
        else:
            print("Неверный ввод, попробуй еще раз.\n")


if __name__ == "__main__":
    main_menu()
