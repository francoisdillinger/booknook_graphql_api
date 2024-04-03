import json
import uuid
from books_data import books_data
from users_data import users_data
# def add_book_id(book_data):
#     book_data["book_id"] = str(uuid.uuid4())
#     return book_data

# def generate_python_code(books_data):
#     python_code = "books_data = [\n"
#     for book in books_data:
#         python_code += "    " + str(book) + ",\n"
#     python_code += "]\n"
#     return python_code

# def main():
#     # Add book_id to each book
#     modified_books_data = [add_book_id(book) for book in books_data]
    
#     # Generate Python code
#     python_code = generate_python_code(modified_books_data)
    
#     # Write Python code to a new file
#     with open("book_data.py", "w") as file:
#         file.write(python_code)


def add_user_id(user):
    user["user_id"] = str(uuid.uuid4())
    return user

def main():
    modified_users = [add_user_id(user) for user in users_data]

    with open("modified_users.py", "w") as file:
        file.write("users = [\n")
        for user in modified_users:
            file.write("    " + str(user) + ",\n")
        file.write("]\n")


if __name__ == "__main__":
    main()

