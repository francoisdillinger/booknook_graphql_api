from langchain.llms import OpenAI
from dotenv import load_dotenv
from books_data import books_data as books
import json

load_dotenv()

# Create an OpenAI object with the API key
llm = OpenAI(
    model='gpt-3.5-turbo-instruct'
)

def generate_long_descriptions( books):
    new_books = []
    for book in books:
        prompt = f'Imagine you are a literary critic and you are being hired to read books and write detailed descriptions in a manner that would interest new readers to read the book in question. I need you to return a two paragraph description of the book ${book["book_title"]}. Make sure new paragraphs have a new line character.'
        result = llm(prompt)
        order = {
            'book_title':book['book_title'],
            'page_count':book['page_count'],
            'publish_date':book['publish_date'],
            'price':book['price'],
            'short_description':book['short_description'],
            'long_description': result,
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
