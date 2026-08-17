import requests
from bs4 import BeautifulSoup
import pandas as pd


def start_parsing():
    print("Запуск финальной версии скрипта...")
    # Твоя правильная прямая ссылка
    url = 'https://books.toscrape.com/'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        books_data = []

        books = soup.find_all('article', class_='product_pod')

        print(f"Статус подключения: {response.status_code}")
        print(f"Удалось поймать книг по твоей ссылке: {len(books)}")

        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            availability = book.find('p', class_='instock availability').text.strip()

            books_data.append({
                'Название': title,
                'Цена': price,
                'Наличие': availability
            })

        if books_data:
            df = pd.DataFrame(books_data)
            df.to_excel('result_books.xlsx', index=False)
            print("Миссия завершена! Файл result_books.xlsx успешно создан и заполнен данными.")
        else:
            print("Список пуст, проверь структуру тегов.")

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    start_parsing()
