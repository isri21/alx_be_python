class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author
		self.__is_checked_out = False
	def get_check_value(self):
		return self.__is_checked_out

class Library:
	def __init__(self):
		self.__books = []
		
	def add_book(self, book):
		book_lf = [book.title, book.author, book.get_check_value()]
		self.__books.append(book_lf)
		
	def check_out_book(self, title):
		i = 0
		for book in self.__books:
			if title in book:
				self.__books[i][2] = True
			else:
				i += 1
				
	def return_book(self, title):
		i = 0
		for book in self.__books:
			if title in book:
				self.__books[i][2] = False
			else:
				i += 1
				
	def list_available_books(self):
		for book in self.__books:
			if False in book:
				print(f"{book[0]} by {book[1]}")
