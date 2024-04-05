from graphene import UUID, Float, ObjectType, String, Int, List, Field, Enum
from sqlalchemy import Numeric
# from app.db.database import db
# from app.db.models import User, Author, Book


class UserObject(ObjectType):
    id = UUID()
    user_name = String()
    password = String()
    email = String()
    first_name = String()
    last_name = String()
    role = String()
    reviews = List(lambda: ReviewObject)
    cart = List(lambda: CartObject)
    orders = List(lambda: OrderObject)

    # Field-level Resolver
    def resolve_reviews(root, info):
        return root.reviews

    # Field-level Resolver
    def resolve_cart(root, info):
        return root.cart

    # Field-level Resolver
    def resolve_orders(root, info):
        return root.orders


class AuthorObject(ObjectType):
    id = UUID()
    author_first_name = String()
    author_last_name = String()
    books = List(lambda: BookObject)

    # Field-level Resolver
    def resolve_books(root, info):
        # This is how you would do it without the back_populates relationship
        # books = db.session.query(Book).filter(Book.author_id == root.id).all()
        # db.session.close()
        # return books

        # This is how you would do it with the back_populates relationship specified in the Book model
        return root.books


class BookObject(ObjectType):
    id = UUID()
    book_title = String()
    page_count = Int()
    publish_date = String()
    price = Float()
    description = String()
    inventory_count = Int()
    isbn = String()
    author = Field(lambda: AuthorObject)
    book_reviews = List(lambda: ReviewObject)
    book_categories = List(lambda: BookCategoriesObject)
    book_orders = List(lambda: OrderObject)

    # Field-level Resolver
    def resolve_author(root, info):
        # This is how you would do it without the back_populates relationship
        # author = db.session.query(Author).filter(Author.id == root.author_id).first()
        # db.session.close()
        # return author

        # This is how you would do it with the back_populates relationship specified in the Author model
        return root.author
    
    def resolve_book_reviews(root, info):
        return root.book_reviews

        # Field-level Resolver
    def resolve_book_categories(root, info):
        return root.book_categories
    
    def resolve_book_orders(root, info):
        return root.book_orders
    

class ReviewObject(ObjectType):
    id = UUID()
    user = Field(lambda: UserObject)
    rating = Int()
    review = String()
    book = Field(lambda: BookObject)

    # Field-level Resolver
    def resolve_user(root, info):
        return root.user

    # Field-level Resolver
    def resolve_book(root, info):
        return root.book


class CategoryObject(ObjectType):
    id = UUID()
    category_name = String()
    books = List(lambda: BookObject)

    # Field-level Resolver
    def resolve_books(root, info):
        return root.books


class BookCategoriesObject(ObjectType):
    id = UUID()
    book_id = Int()
    category_id = Int()
    book = Field(lambda: BookObject)
    category = Field(lambda: CategoryObject)

    # Field-level Resolver
    def resolve_book(root, info):
        return root.book

    # Field-level Resolver
    def resolve_category(root, info):
        return root.category
    

class CartObject(ObjectType):
    id = UUID()
    user_id = Int()
    book_id = Int()
    quantity = Int()
    book = Field(lambda: BookObject)
    user = Field(lambda: UserObject)

    # Field-level Resolver
    def resolve_book(root, info):
        return root.book

    # Field-level Resolver
    def resolve_user(root, info):
        return root.user
    

class OrderStatusEnum(Enum):
    PROCESSING = 'Processing'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'


class OrderObject(ObjectType):
    # order_id = UUID()
    # This also has an 'id' for uniqueness but 'order_id' is a shared id by items of same order
    order_id = UUID()
    user_id = UUID()
    book_id = UUID()
    quantity = Int()
    order_date = String()
    order_amount = Float()
    order_status = Field(OrderStatusEnum)

    book = Field(lambda: BookObject)
    user = Field(lambda: UserObject)

    # Field-level Resolver
    def resolve_book(root, info):
        return root.book

    # Field-level Resolver
    def resolve_user(root, info):
        return root.user
   
    
class WishListObject(ObjectType):
    id = UUID()
    user_id = Int()
    book_id = Int()
    book = Field(lambda: BookObject)
    user = Field(lambda: UserObject)

    # Field-level Resolver
    def resolve_book(root, info):
        return root.book

    # Field-level Resolver
    def resolve_user(root, info):
        return root.user