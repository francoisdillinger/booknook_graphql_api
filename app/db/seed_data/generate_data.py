# from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from books_data import books_data as books
import json

load_dotenv()

# Create an OpenAI object with the API key
chat = ChatOpenAI(model="gpt-4")

def generate_long_descriptions( books):
    count = 1
    new_books = []
    for book in books:
        systemPrompt = "You are an editor hired to read books and write detailed descriptions in a manner that would encourage new customers to purchase the book in question. You don't write reviews, you write synopses."
        userPrompt = f'I need you to return a three paragraph synopsis of the book ${book["book_title"]}. Be Detailed!'

        messages = [
            SystemMessage(content=systemPrompt),
            HumanMessage(content=userPrompt),
        ]
        response = chat.invoke(messages)
        order = {
            'book_title':book['book_title'],
            'page_count':book['page_count'],
            'publish_date':book['publish_date'],
            'price':book['price'],
            'short_description':book['short_description'],
            'long_description': response.content,
            'inventory_count':book['inventory_count'],
            'isbn': book['isbn'],
            'author_id':book['author_id'],
            'book_id':book['book_id']
        }
        new_books.append(order)
        count+=1
        print(f'Book {count} finished.')
    return new_books

books_with_long_descriptions = generate_long_descriptions(books)

with open("long_description.py", "w", encoding='utf-8', errors='replace') as file:
    file.write("books = [\n")
    for book in books_with_long_descriptions:
        file.write("    " + str(book) + ",\n")
    file.write("]\n")
