from langchain.llms import OpenAI
from dotenv import load_dotenv
from books_data import books_data as books
import json

load_dotenv()

# Create an OpenAI object with the API key
# llm = OpenAI(
#     model='gpt-3.5-turbo-instruct'
# )

# Generate text using the generate method
# result = llm("Return a two paragraph description of the book Frankenstein. Make sure new paragraphs have a new line character. Return description in following json format: {'description': two paragraphs}")
# print(result)


# with open("long_description.py", "w") as file:
#     file.write("random_orders = [\n")
#     # for order in random_orders:
#     file.write("    " + str(result) + ",\n")
#     file.write("]\n")



def generate_long_descriptions( books):
    new_books = []
    for book in books:
        order = {
            'book_title':book['book_title'],
            'page_count':book['page_count'],
            'publish_date':book['publish_date'],
            'price':book['price'],
            'short_description':book['short_description'],
            'inventory_count':book['inventory_count'],
            'isbn': book['isbn'],
            'author_id':book['author_id'],
            'book_id':book['book_id']
        }
        new_books.append(order)
    return new_books

books_with_long_descriptions = generate_long_descriptions(books)

with open("long_description.py", "w", encoding='utf-8', errors='replace') as file:
    file.write("books = [\n")
    for book in books_with_long_descriptions:
        file.write("    " + str(book) + ",\n")
    file.write("]\n")
