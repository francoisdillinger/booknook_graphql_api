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


# def add_user_id(user):
#     user["user_id"] = str(uuid.uuid4())
#     return user

# def main():
#     modified_users = [add_user_id(user) for user in users_data]

#     with open("modified_users.py", "w") as file:
#         file.write("users = [\n")
#         for user in modified_users:
#             file.write("    " + str(user) + ",\n")
#         file.write("]\n")



# def add_review_id(review):
#     review["review_id"] = str(uuid.uuid4())
#     return review

# def generate_python_code(reviews_data):
#     python_code = "reviews_data = [\n"
#     for review in reviews_data:
#         python_code += "    " + str(review) + ",\n"
#     python_code += "]\n"
#     return python_code

# def main():
#     # Add review_id to each review
#     modified_reviews_data = [add_review_id(review) for review in book_reviews_data.reviews_data]
    
#     # Generate Python code
#     python_code = generate_python_code(modified_reviews_data)
    
#     # Write Python code to a new file
#     with open("modified_reviews.py", "w") as file:
#         file.write(python_code)


# if __name__ == "__main__":
#     main()



def add_category_id(book_category):
    book_category["id"] = str(uuid.uuid4())
    return book_category

def generate_python_code(book_categories_data):
    python_code = "book_categories_data = [\n"
    for book_category in book_categories_data:
        python_code += "    " + str(book_category) + ",\n"
    python_code += "]\n"
    return python_code

def main():
    # Assuming book_categories_data is a list of dictionaries from book_category_data.py
    from book_category_data import book_category_data
    
    # Add category_id to each book category
    modified_book_categories_data = [add_category_id(book_category) for book_category in book_category_data]
    
    # Generate Python code
    python_code = generate_python_code(modified_book_categories_data)
    
    # Write Python code to a new file
    with open("modified_book_categories.py", "w") as file:
        file.write(python_code)

if __name__ == "__main__":
    main()