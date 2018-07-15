

# Brian Drinkwater
# TomeRater Project, Code Academy Intensives, "Programming with Python"
# Date - July 15th, 2018
# Thank YOU!!  to ALL Moderators who helped me along the way



# ================   User Class ==========================

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_email_address):
         self.email = new_email_address
         return "Your email address {} has been updated".format(self.email)

    def __repr__(self):
        return "User {}, Email: {}, total books read {}".format(self.name, self.email, len(self.books))

# compare users, if they have same name and email address they are same
    def __eq__(self, other_user):
        if other_user.email == self.email and other_user.name == self.name:
            return True
        else:
            return False
    
    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        average_rating = 0
        books_rated = 0
        for value in self.books.values():
            if value:
                average_rating += value
                books_rated += 1
        average_rating = average_rating/books_rated
        return average_rating




#===============  Book Class ============================


class Book:
    isbn_lst = []
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        Book.isbn_lst.append(self.isbn) # append each books isbn to list above, list is used to check for duplicates


# return the title of the book with .title() method
    def get_title():
        return self.title.title()

# return the isbn of the book
    def get_isbn():
        return self.isbn

    def set_isbn(self, isbn):
        if Book.isbn_check(isbn): # check isbn against isbn_lst for uniqueness
            return
        self.isbn = isbn
        return "The ISBN for \"{}\" has been set to: {}.".format(self.title, self.isbn)
    
#add rating of book to the self.rating list
    def add_rating(self, rating):
        #self.rating = rating
        if rating and rating > 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            return "Invalid Rating"

#use comparison method to compare isbn and title 
    def __eq__(self, new_book):
        if (self.isbn == new_book.isbn) and (self.title == new_book.title):
            return True
        else:
            return False

    def get_average_rating(self):
        ratings = 0
        for rating in self.ratings:
            ratings += rating
            ratings = ratings / len(self.ratings)
        return ratings

    def isbn_check(isbn): # Get Creative (bullet point 2) Check isbn_lst for duplicates
        if isbn in Book.isbn_lst:
            print("That ISBN already exists in the system")
            return True
        return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title



#================  Fiction Book Class ========================


class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return " {} by {}".format(self.title, self.author)



#============= Non Fiction Book ============================


class Non_Fiction(Book):

    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject():
        #return the subject of the book
        return self.subject

    def get_level():
        # return the reading level
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}.".format(self.title, self.level, self.subject)


#=================  TomeRater Class =======================


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        if Book.isbn_check(isbn): # check isbn # against isbn_lst for uniqueness
            return
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        if Book.isbn_check(isbn): # check isbn # against isbn_lst for uniqueness
            #print("it checked for the isbn:")
            return
        new_fiction = Fiction(title, author, isbn)
        #new_fiction = Fiction(isbn)
        return new_fiction

    def create_non_fiction(self, title, subject, level, isbn):
        if Book.isbn_check(isbn):  # check isbn # against isbn_lst for uniqueness
            return
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating = None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books.keys():
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)

        else:
            return "No user with email {}!".format(self.email)


    def add_user(self, name, email, user_books = None):
        # Get Creative - (bullet points 1 and 3) - Check to see if user being added  has valid email syntax and email address is not already in system)
        if not self.check_for_valid_email(email):
            print("The email address is invalid. Please check that it has proper syntax 'user@' and the suffix ends with one of these{d}".format(d=['com']))
            return
        if email in self.users:
            print("A user with that email address already exists, please try adding a differnet address")
            return
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)



#==================  Analysis Methods =================


    def print_catalog(self):
        for book_name in self.books:
            print(book_name)

    def print_users(self):
        for value in self.users.values():
            print(value)


    def most_read_book(self):
        book_read = None
        book_value = 0
        for book in self.books:
            each_book = self.books[book]
            if each_book > book_value:
                book_value = each_book
                book_read = book
        return book_read


    def highest_rated_book(self):
        book_rating = 0
        best_rated_book = None
        for book in self.books:
            average = book.get_average_rating()
            if average > book_rating:
                book_rating = average
                best_rated_book = book
        return best_rated_book

    def most_positive_user(self):
        high_rating = 0
        user_rated = None
        for user in self.users.values():
            highest_avg = user.get_average_rating()
            if highest_avg > high_rating:
                high_rating = highest_avg
                user_rated = user
        return user_rated

    def get_most_read_book(self):
        most_read_book = None
        num_times_read = 0
        for book in self.books:
            book_read = self.books[book]
            if book_read > num_times_read:
                num_times_read = book_read
                most_read_book = book
        return "The book:{} was read a total of \"{}\" times.".format(most_read_book, num_times_read) 

    def check_for_valid_email(self, email):
        domain_suffix = ['com', 'edu', 'org']
        dot_notation = email.split('.')[-1]
        if ('@' in email) and (dot_notation in domain_suffix):
            #return "Your email address is valid"
            return True
        else:
            #return "The email address is invalid. Please check that it has proper syntax 'user@' and the suffix ends with one of these{d}".format(d=domain_suffix) 
            return False




