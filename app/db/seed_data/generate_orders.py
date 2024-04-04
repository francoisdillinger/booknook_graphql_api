import uuid
import random
from datetime import datetime, timedelta
import json
from books_data import books_data as books
from users_data import users_data as users

# Define users
# users = [
#     {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805'},
#     {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88'},
#     {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192'},
#     {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b'},
#     {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641'},
#     {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7'},
#     {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b'},
#     {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17'},
#     {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee'},
#     {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e'}
# ]

# Define books
# books = [
#     {'book_title': 'The Alchemist', 'price': 14.95, 'book_id': '94214347-e2c1-4fa4-872f-2b02dfaccfef'},
#     {'book_title': 'Pride and Prejudice', 'price': 9.99, 'book_id': '4e693a90-d582-421b-afbf-a4babf10a68e'},
#     {'book_title': 'Adventures of Huckleberry Finn', 'price': 8.99, 'book_id': '5868f357-1e51-4383-a603-b21dd5881b18'}
# ]

# Function to generate random order date within the last 3 years
def generate_random_order_date():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365 * 3)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime("%Y-%m-%d")

# Function to generate random orders
def generate_random_orders(users, books):
    orders = []
    for user in users:
        for _ in range(random.randint(1, 50)):  # Random number of orders per user
            order_id = str(uuid.uuid4())
            order_date = generate_random_order_date()
            order_books = random.sample(books, random.randint(1, 5))  # Random books for each order
            for book in order_books:
                quantity = random.randint(1, 5)
                order_amount = book['price'] * quantity
                order = {
                    'order_id': order_id,
                    'user_id': user['user_id'],
                    'book_id': book['book_id'],
                    'quantity': quantity,
                    'order_date': order_date,
                    'order_amount': round(order_amount, 2)
                }
                orders.append(order)
    return orders

# Generate random orders
random_orders = generate_random_orders(users, books)

# Write random orders to a Python file
with open("modified_orders.py", "w") as file:
    file.write("random_orders = [\n")
    for order in random_orders:
        file.write("    " + str(order) + ",\n")
    file.write("]\n")

print("Random orders written to modified_orders.py file.")
