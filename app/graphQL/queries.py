from graphene import ObjectType, List
from app.db.database import db
from app.graphQL.types import (
    UserObject, 
    AuthorObject, 
    BookObject, 
    ReviewObject, 
    CategoryObject, 
    BookCategoriesObject, 
    CartObject,
    OrderObject
    )
from app.db.models import (
    User, 
    Author, 
    Book, 
    Review, 
    Categories, 
    BookCategories, 
    Cart, 
    Order
    )


class Query(ObjectType):
    users = List(UserObject)
    authors = List(AuthorObject)
    books = List(BookObject)
    reviews = List(ReviewObject)
    categories = List(CategoryObject)
    book_categories = List(BookCategoriesObject)
    cart = List(CartObject)
    orders = List(OrderObject)



    # Root-Level Resolvers
    def resolve_users(root, info):
        return db.session.query(User).all()
    
    def resolve_authors(root, info):
        return db.session.query(Author).all()
    
    def resolve_books(root, info):
        return db.session.query(Book).all()
    
    def resolve_reviews(root, info):
        return db.session.query(Review).all()
    
    def resolve_categories(root, info):
        return db.session.query(Categories).all()
    
    def resolve_book_categories(root, info):
        return db.session.query(BookCategories).all()
    
    def resolve_cart(root, info):
        return db.session.query(Cart).all()
    
    def resolve_orders(root, info): 
        return db.session.query(Order).all()