from graphene import ObjectType, List, Field, ID, String
from app.db.database import db
from app.graphQL.types import (
    UserObject, 
    AuthorObject, 
    BookObject, 
    ReviewObject, 
    CategoryObject, 
    BookCategoriesObject, 
    CartObject,
    OrderObject,
    WishListObject
    )
from app.db.models import (
    User, 
    Author, 
    Book, 
    Review, 
    Categories, 
    BookCategories, 
    Cart, 
    Order,
    WishList
    )


class Query(ObjectType):
    # List queries
    users = List(UserObject)
    authors = List(AuthorObject)
    books = List(BookObject)
    reviews = List(ReviewObject)
    categories = List(CategoryObject)
    book_categories = List(BookCategoriesObject)
    cart = List(CartObject)
    orders = List(OrderObject)
    wish_list = List(WishListObject)

    # Single item queries
    user = Field(UserObject, id=ID(required=True))
    author = Field(AuthorObject, id=ID(required=True))
    book = Field(BookObject, id=ID(required=True))
    review = Field(ReviewObject, id=ID(required=True))
    category = Field(CategoryObject, id=ID(required=True))
    book_category = Field(BookCategoriesObject, id=ID(required=True))
    cart_item = Field(CartObject, id=ID(required=True))
    order = Field(OrderObject, id=ID(required=True))
    wish_list_item = Field(WishListObject, id=ID(required=True))
    
    # Additional queries by unique fields (e.g., username, book title)
    user_by_name = Field(UserObject, user_name=String(required=True))
    book_by_title = Field(BookObject, book_title=String(required=True))

    # Root-Level Resolvers for lists
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
    
    def resolve_wish_list(root, info):
        return db.session.query(WishList).all()

    # Resolvers for single items by ID
    def resolve_user(root, info, id):
        return db.session.query(User).get(id)
    
    def resolve_author(root, info, id):
        return db.session.query(Author).get(id)
    
    def resolve_book(root, info, id):
        return db.session.query(Book).get(id)
    
    def resolve_review(root, info, id):
        return db.session.query(Review).get(id)
    
    def resolve_category(root, info, id):
        return db.session.query(Categories).get(id)
    
    def resolve_book_category(root, info, id):
        return db.session.query(BookCategories).get(id)
    
    def resolve_cart_item(root, info, id):
        return db.session.query(Cart).get(id)
    
    def resolve_order(root, info, id):
        return db.session.query(Order).get(id)
    
    def resolve_wish_list_item(root, info, id):
        return db.session.query(WishList).get(id)
    
    # Resolvers for single items by unique fields
    def resolve_user_by_name(root, info, user_name):
        return db.session.query(User).filter(User.user_name == user_name).first()
    
    def resolve_book_by_title(root, info, book_title):
        return db.session.query(Book).filter(Book.book_title == book_title).first()
