import requests
from bs4 import BeautifulSoup

choice = '8'

while choice != '0':

    choice = input("""
    Welcome to the Bookstore, Please choose a genre to browse...
    1.) Mystery
    2.) Philosophy
    3.) Science Fiction
    4.) Horror
    5.) Poetry
    0.) Quit
    """)

    if choice == '1':
        # Request the html page of the mystery section and locate each book element
        mystery_text = requests.get('https://books.toscrape.com/catalogue/category/books/mystery_3/index.html').text
        mystery_soup = BeautifulSoup(mystery_text, 'lxml')
        mystery_books = mystery_soup.find_all('article', class_='product_pod')

        print("---MYSTERY---")

        print("""
        1.) Browse all
        2.) Search for a book""")
        menu = input()

        # Browse all mystery books
        if menu == '1':
            for item in mystery_books:
                title = item.find('h3', class_=False).text
                price = item.find('p', class_='price_color').text
                price = '$' + price[2:]
                available = item.find('p', class_='instock availability').text
                available = available.strip()

                print('Title: ' + title)
                print('Price: ' + price)
                print('Availability: ' + available)
                print('-----------------------------------')
        # Search Mystery Books
        if menu == '2':
            by_name = input("Enter book name to search for: ")

            for item in mystery_books:
                title = item.find('h3', class_=False).text
                price = item.find('p', class_='price_color').text
                price = '$' + price[2:]
                available = item.find('p', class_='instock availability').text
                available = available.strip()

                if by_name.upper() in title.upper():
                    print('Title: ' + title)
                    print('Price: ' + price)
                    print('Availability: ' + available)
                    print('---------------------------------------------')
# ---------------------------------------------------------------------------------------
    if choice == '2':

        phil_text = requests.get('https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html').text
        phil_soup = BeautifulSoup(phil_text, 'lxml')
        phil_books = phil_soup.find_all('article', class_='product_pod')

        print("---PHILOSOPHY---")

        print("""
                1.) Browse all
                2.) Search for a book""")
        menu = input()

        # Browse all philosophy books
        if menu == '1':
            for item in phil_books:
                title = item.find('h3', class_=False).text
                price = item.find('p', class_='price_color').text
                price = '$' + price[2:]
                available = item.find('p', class_='instock availability').text
                available = available.strip()

                print('Title: ' + title)
                print('Price: ' + price)
                print('Availability: ' + available)
                print('-----------------------------------')

        # Search Philosophy Books
        if menu == '2':
            by_name = input("Enter book name to search for: ")

            for item in phil_books:
                title = item.find('h3', class_=False).text
                price = item.find('p', class_='price_color').text
                price = '$' + price[2:]
                available = item.find('p', class_='instock availability').text
                available = available.strip()

                if by_name.upper() in title.upper():
                    print('Title: ' + title)
                    print('Price: ' + price)
                    print('Availability: ' + available)
                    print('---------------------------------------------')
# ---------------------------------------------------------------------------------------
    if choice == '3':
        scifi_text = requests.get(
            'https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html').text
        scifi_soup = BeautifulSoup(scifi_text, 'lxml')
        scifi_books = scifi_soup.find_all('article', class_='product_pod')

        print("---SCIENCE FICTION---")
        print("""
                1.) Browse all
                2.) Search for a book""")
        menu = input()

        # Browse all Science Fiction books
        if menu == '1':
            for item in scifi_books:
                title = item.find('h3', class_=False).text
                price = item.find('p', class_='price_color').text
                price = '$' + price[2:]
                available = item.find('p', class_='instock availability').text
                available = available.strip()

                print('Title: ' + title)
                print('Price: ' + price)
                print('Availability: ' + available)
                print('-----------------------------------')

        # Search for Science Fiction Books
        if menu == '2':
            by_name = input("Enter book name to search for: ")

            for item in scifi_books:
                title = item.find('h3', class_=False).text
                price = item.find('p', class_='price_color').text
                price = '$' + price[2:]
                available = item.find('p', class_='instock availability').text
                available = available.strip()

                if by_name.upper() in title.upper():
                    print('Title: ' + title)
                    print('Price: ' + price)
                    print('Availability: ' + available)
                    print('---------------------------------------------')

# ---------------------------------------------------------------------------------------
    if choice == '4':
        horror_text = requests.get('https://books.toscrape.com/catalogue/category/books/horror_31/index.html').text
        horror_soup = BeautifulSoup(horror_text, 'lxml')
        horror_books = horror_soup.find_all('article', class_='product_pod')

        print("---HORROR---")
        print("""
        1.) Browse all
        2.) Search for a book""")
        menu = input()

        # Browse all Horror books
        if menu == '1':
            for item in horror_books:
                title = item.find('h3', class_=False).text
                price = item.find('p', class_='price_color').text
                price = '$' + price[2:]
                available = item.find('p', class_='instock availability').text
                available = available.strip()

                print('Title: ' + title)
                print('Price: ' + price)
                print('Availability: ' + available)
                print('-----------------------------------')

        # Search for Horror Books
        if menu == '2':
            by_name = input("Enter book name to search for: ")

            for item in horror_books:
                title = item.find('h3', class_=False).text
                price = item.find('p', class_='price_color').text
                price = '$' + price[2:]
                available = item.find('p', class_='instock availability').text
                available = available.strip()

                if by_name.upper() in title.upper():
                    print('Title: ' + title)
                    print('Price: ' + price)
                    print('Availability: ' + available)
                    print('---------------------------------------------')
# ---------------------------------------------------------------------------------------
    if choice == '5':
        poetry_text = requests.get('https://books.toscrape.com/catalogue/category/books/poetry_23/index.html').text
        poetry_soup = BeautifulSoup(poetry_text, 'lxml')
        poetry_books = poetry_soup.find_all('article', class_='product_pod')

        print("---POETRY---")
        print("""
        1.) Browse all
        2.) Search for a book""")
        menu = input()

        # Browse all Poetry books
        if menu == '1':
            for item in poetry_books:
                title = item.find('h3', class_=False).text
                price = item.find('p', class_='price_color').text
                price = '$' + price[2:]
                available = item.find('p', class_='instock availability').text
                available = available.strip()

                print('Title: ' + title)
                print('Price: ' + price)
                print('Availability: ' + available)
                print('-----------------------------------')

        # Search for Poetry Books
        if menu == '2':
            by_name = input("Enter book name to search for: ")

            for item in poetry_books:
                title = item.find('h3', class_=False).text
                price = item.find('p', class_='price_color').text
                price = '$' + price[2:]
                available = item.find('p', class_='instock availability').text
                available = available.strip()

                if by_name.upper() in title.upper():
                    print('Title: ' + title)
                    print('Price: ' + price)
                    print('Availability: ' + available)
                    print('---------------------------------------------')

