from graphene import Mutation, String, Int, Field, ObjectType
from app.db.database import db
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound
from graphql import GraphQLError
from app.graphQL.types import (
    UserObject, 
    AuthorObject, 
    BookObject, 
    CategoryObject, 
    BookCategoriesObject, 
    CartObject, 
    OrderObject, 
    ReviewObject
    )
from app.db.models import (
    User, 
    Author, 
    Book, 
    Categories, 
    BookCategories, 
    Cart, 
    Order, 
    Review
    )



class AddUser(Mutation):
    class Arguments:
        user_name = String(required=True)
        password = String(required=True)
        email = String(required=True)
        first_name = String(required=True)
        last_name = String(required=True)
        role = String(required=True)
    
    user = Field(lambda: UserObject)

    def mutate(root, info, user_name, password, email, first_name, last_name, role):
        user = User(
            user_name=user_name,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role
        )
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        return AddUser(user=user)
    

class UpdateUser(Mutation):
    class Arguments:
        user_id = Int(required=True)
        user_name = String()
        password = String()
        email = String()
        first_name = String()
        last_name = String()
        role = String()
    
    user = Field(lambda: UserObject)

    def mutate(root, info, user_id, user_name=None, password=None, email=None, first_name=None, last_name=None, role=None):
        user = db.session.query(User).filter(User.id == user_id).first()

        if not user:
            raise GraphQLError(f'User with id {user_id} not found.')

        if user_name:
            user.user_name = user_name
        if password:
            user.password = password
        if email:
            user.email = email
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if role:
            user.role = role

        db.session.commit()
        db.session.refresh(user)
        return UpdateUser(user=user)
    

class DeleteUser(Mutation):
    class Arguments:
        user_id = Int(required=True)
    
    user = Field(lambda: UserObject)

    def mutate(root, info, user_id):
        user = db.session.query(User).filter(User.id == user_id).first()

        if not user:
            raise GraphQLError(f'User with id {user_id} not found.')

        db.session.delete(user)
        db.session.commit()
        return DeleteUser(user=user)


class AddAuthor(Mutation):
    class Arguments:
        author_first_name = String(required=True)
        author_last_name = String(required=True)
    
    author = Field(lambda: AuthorObject)

    def mutate(root, info, author_first_name, author_last_name):
        author = Author(
            author_first_name=author_first_name,
            author_last_name=author_last_name
        )
        db.session.add(author)
        db.session.commit()
        db.session.refresh(author)
        return AddAuthor(author=author)


class UpdateAuthor(Mutation):
    class Arguments:
        author_id = Int(required=True)
        author_first_name = String()
        author_last_name = String()
    
    author = Field(lambda: AuthorObject)

    def mutate(root, info, author_id, author_first_name=None, author_last_name=None):
        # This is how you would do it if the session is being closed prematurely. I removed explicit closing of 
        # the session in mutations because it was causing issues and flask_sqlalchemy handles it for us.
        # author = db.session.query(Author).options(joinedload(Author.books)).filter(Author.id == author_id).first()

        
        author = db.session.query(Author).filter(Author.id == author_id).first()

        if not author:
            raise GraphQLError(f'Author with id {author_id} does not exist.')
        if author_first_name is not None:
            author.author_first_name = author_first_name
        if author_last_name is not None:
            author.author_last_name = author_last_name

        db.session.commit()
        db.session.refresh(author)
        return UpdateAuthor(author=author)


class DeleteAuthor(Mutation):
    class Arguments:
        author_id = Int(required=True)
    
    author = Field(lambda: AuthorObject)

    def mutate(root, info, author_id):
        author = db.session.query(Author).filter(Author.id == author_id).first()

        if not author:
            raise GraphQLError(f'Author with id {author_id} does not exist.')

        db.session.delete(author)
        db.session.commit()
        return DeleteAuthor(author=author)
    
    
class AddBook(Mutation):
    class Arguments:
        book_title = String(required=True)
        page_count = Int(required=True)
        publish_date = String(required=True)
        price = Int(required=True)
        description = String(required=True)
        inventory_count = Int(required=True)
        isbn = String(required=True)
        author_id = Int(required=True)

    book = Field(lambda: BookObject)

    def mutate(root, info, book_title, page_count, publish_date, price, description, inventory_count, isbn, author_id):
        try:
            author = db.session.query(Author).filter(Author.id == author_id).one()
        except NoResultFound:
            # Handle the error, for example by returning a GraphQL error:
            raise GraphQLError('The provided author_id does not exist')
        
        book = Book(
            book_title=book_title,
            page_count=page_count,
            publish_date=publish_date,
            price=price,
            description=description,
            inventory_count=inventory_count,
            isbn=isbn,
            author_id=author_id
        )
        db.session.add(book)
        db.session.commit()
        db.session.refresh(book)
        return AddBook(book=book)


class UpdateBook(Mutation):
    class Arguments:
        book_id = Int(required=True)
        book_title = String()
        page_count = Int()
        publish_date = String()
        price = Int()
        description = String()
        inventory_count = Int()
        isbn = String()
        author_id = Int()

    book = Field(lambda: BookObject)

    def mutate(root, info, book_id, book_title=None, page_count=None, publish_date=None, price=None, description=None, inventory_count=None, isbn=None, author_id=None):
        book = db.session.query(Book).filter(Book.id == book_id).first()

        if not book:
            raise GraphQLError(f'Book with id {book_id} does not exist.')
        if book_title is not None:
            book.book_title = book_title
        if page_count is not None:
            book.page_count = page_count
        if publish_date is not None:
            book.publish_date = publish_date
        if price is not None:
            book.price = price
        if description is not None:
            book.description = description
        if inventory_count is not None:
            book.inventory_count = inventory_count
        if isbn is not None:
            book.isbn = isbn
        if author_id is not None:
            book.author_id = author_id

        db.session.commit()
        db.session.refresh(book)
        return UpdateBook(book=book) 


class DeleteBook(Mutation):
    class Arguments:
        book_id = Int(required=True)
    
    book = Field(lambda: BookObject)

    def mutate(root, info, book_id):
        book = db.session.query(Book).filter(Book.id == book_id).first()

        if not book:
            raise GraphQLError(f'Book with id {book_id} does not exist.')

        db.session.delete(book)
        db.session.commit()
        return DeleteBook(book=book)


class AddCategory(Mutation):
    class Arguments:
        category_name = String(required=True)
    
    category = Field(lambda: CategoryObject)

    def mutate(root, info, category_name):
        category = Categories(
            category_name=category_name
        )
        db.session.add(category)
        db.session.commit()
        db.session.refresh(category)
        return AddCategory(category=category)


class UpdateCategory(Mutation):
    class Arguments:
        category_id = Int(required=True)
        category_name = String()
    
    category = Field(lambda: CategoryObject)

    def mutate(root, info, category_id, category_name=None):
        category = db.session.query(Categories).filter(Categories.id == category_id).first()

        if not category:
            raise GraphQLError(f'Category with id {category_id} does not exist.')
        if category_name is not None:
            category.category_name = category_name

        db.session.commit()
        db.session.refresh(category)
        return UpdateCategory(category=category)


class AddBookCategory(Mutation):
    class Arguments:
        book_id = Int(required=True)
        category_id = Int(required=True)
    
    book_category = Field(lambda: BookCategoriesObject)

    def mutate(root, info, book_id, category_id):
        try:
            book = db.session.query(Book).filter(Book.id == book_id).one()
        except NoResultFound:
            # Handle the error, for example by returning a GraphQL error:
            raise GraphQLError('The provided book_id does not exist')
        
        try:
            category = db.session.query(Categories).filter(Categories.id == category_id).one()
        except NoResultFound:
            # Handle the error, for example by returning a GraphQL error:
            raise GraphQLError('The provided category_id does not exist')
        
        book_category = BookCategories(
            book_id=book_id,
            category_id=category_id
        )
        db.session.add(book_category)
        db.session.commit()
        db.session.refresh(book_category)
        return AddBookCategory(book_category=book_category)

# Not sure if this is needed, it seems to be cuasing an issue where it is changing the category ID
# only for the book selected. In other words, it allows duplication of a book's categories, and
# we don't want that behavior. Categories simply need to be added or deleted, not modified.

# class UpdateBookCategory(Mutation):
#     class Arguments:
#         book_category_id = Int(required=True)
#         book_id = Int()
#         category_id = Int()
    
#     book_category = Field(lambda: BookCategoriesObject)

#     def mutate(root, info, book_category_id, book_id=None, category_id=None):
#         book_category = db.session.query(BookCategories).filter(BookCategories.id == book_category_id).first()
#         book = db.session.query(Book).filter(Book.id == book_id).first()

#         if not book_category:
#             raise GraphQLError(f'BookCategory with id {book_category_id} does not exist.')
#         if not book:
#             raise GraphQLError(f'Book with id {book_id} does not exist.')
#         if book_id is not None:
#             book_category.book_id = book_id
#         if category_id is not None:
#             book_category.category_id = category_id

#         db.session.commit()
#         db.session.refresh(book_category)
#         return UpdateBookCategory(book_category=book_category)


class DeleteBookCategories(Mutation):
    class Arguments:
        book_id = Int(required=True)
    
    book_category = Field(lambda: BookCategoriesObject)

    def mutate(root, info, book_id):
        # Make sure the book exists
        book = db.session.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise GraphQLError(f'Book with id {book_id} does not exist.')
        
        # Make sure the BookCategories record exists
        book_categories = db.session.query(BookCategories).filter(BookCategories.book_id == book_id).all()
        if not book_categories:
            raise GraphQLError(f'BookCategory with book_id {book_id} does not exist.')
        
        # Delete the BookCategories record
        for book_category in book_categories:
            db.session.delete(book_category)

        db.session.commit()

        return DeleteBookCategories(book_category=book_category)


class AddCart(Mutation):
    class Arguments:
        user_id = Int(required=True)
        book_id = Int(required=True)
        quantity = Int(required=True)
    
    cart = Field(lambda: CartObject)

    def mutate(root, info, user_id, book_id, quantity):
        cart = Cart(
            user_id=user_id,
            book_id=book_id,
            quantity=quantity
        )
        db.session.add(cart)
        db.session.commit()
        db.session.refresh(cart)
        return AddCart(cart=cart)
    

class UpdateCart(Mutation):
    class Arguments:
        cart_id = Int(required=True)
        quantity = Int(required=True)
    
    cart = Field(lambda: CartObject)

    def mutate(root, info, cart_id, quantity):
        cart = db.session.query(Cart).filter(Cart.id == cart_id).first()

        if not cart:
            raise GraphQLError(f'Cart item with id {cart_id} does not exist.')
        
        cart.quantity = quantity
        db.session.commit()
        db.session.refresh(cart)
        return UpdateCart(cart=cart)


class DeleteCart(Mutation):
    class Arguments:
        cart_id = Int(required=True)
    
    cart = Field(lambda: CartObject)

    def mutate(root, info, cart_id):
        cart = db.session.query(Cart).filter(Cart.id == cart_id).first()

        if not cart:
            raise GraphQLError(f'Cart item with id {cart_id} does not exist.')
        
        db.session.delete(cart)
        db.session.commit()

        return DeleteCart(cart=cart)


class AddOrder(Mutation):
    class Arguments:
        order_id = String(required=True)
        user_id = Int(required=True)
        book_id = Int(required=True)
        quantity = Int(required=True)
        order_date = String(required=True)
        # Come back and make sure you add a book price as we need to calculate the total price of the order
        # based on the current price of the book at the time or ordering since prices fluctuate in the real world.

    order = Field(lambda: OrderObject)

    def mutate(root, info, user_id, book_id, quantity, order_date, order_id):
        order = Order(
            order_id=order_id,
            user_id=user_id,
            book_id=book_id,
            quantity=quantity,
            order_date=order_date
        )
        db.session.add(order)
        db.session.commit()
        db.session.refresh(order)
        return AddOrder(order=order)


class AddReview(Mutation):
    class Arguments:
        user_id = Int(required=True)
        book_id = Int(required=True)
        rating = Int(required=True)
        review = String(required=True)
    
    review = Field(lambda: ReviewObject)

    def mutate(root, info, user_id, book_id, rating, review):
        user = db.session.query(User).filter(User.id == user_id).first()
        book = db.session.query(Book).filter(Book.id == book_id).first()

        if not user:
            raise GraphQLError(f'User with id {user_id} does not exist.')
        if not book:
            raise GraphQLError(f'Book with id {book_id} does not exist.')
        if rating < 1 or rating > 5:
            raise GraphQLError(f'Rating must be between 1 and 5.')
        
        review = Review(
            user_id=user_id,
            book_id=book_id,
            rating=rating,
            review=review
        )
        db.session.add(review)
        db.session.commit()
        db.session.refresh(review)
        return AddReview(review=review)


class UpdateReview(Mutation):
    class Arguments:
        # This is the id of the review, not the user or book id
        # Had to change due to issues with testing: review_id vs id
        id = Int(required=True)
        rating = Int()
        review = String()
    
    review = Field(lambda: ReviewObject)

    def mutate(root, info, id, rating=None, review=None):
        review_instance = db.session.query(Review).filter(Review.id == id).first()

        if not review_instance:
            raise GraphQLError(f'Review with id {id} does not exist.')
        if rating is not None:
            if rating < 1 or rating > 5:
                raise GraphQLError(f'Rating must be between 1 and 5.')
            review_instance.rating = rating
        if review is not None:
            review_instance.review = review

        db.session.commit()
        db.session.refresh(review_instance)
        return UpdateReview(review=review_instance) 


class DeleteReview(Mutation):
    class Arguments:
        review_id = Int(required=True)
    
    review = Field(lambda: ReviewObject)

    def mutate(root, info, review_id):
        review = db.session.query(Review).filter(Review.id == review_id).first()

        if not review:
            raise GraphQLError(f'Review with id {review_id} does not exist.')
        
        db.session.delete(review)
        db.session.commit()

        return DeleteReview(review=review)


class Mutation(ObjectType):
    add_user = AddUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

    add_author = AddAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()

    add_book = AddBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()

    add_category = AddCategory.Field()
    update_category = UpdateCategory.Field()
    add_book_category = AddBookCategory.Field()
    # update_book_category = UpdateBookCategory.Field()
    delete_book_category = DeleteBookCategories.Field()

    add_cart = AddCart.Field()
    update_cart = UpdateCart.Field()
    delete_cart = DeleteCart.Field()

    add_order = AddOrder.Field()

    add_review = AddReview.Field()
    update_review = UpdateReview.Field()
    delete_review = DeleteReview.Field()