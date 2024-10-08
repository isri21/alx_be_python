class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author
		self.__is_checked_out = False

	def set_check_value(self, value):
		self.__is_checked_out = value
		
	def return_book(self):
		if self.__is_checked_out == True:
			return True	
	def is_available(self):
		if self.__is_checked_out == False:
			return False

class Library:
	def __init__(self):
		self._books = []
		
	def add_book(self, book):
		self._books.append(book)
		
	def check_out_book(self, title):
		for book in self._books:
			if book.title == title:
				book.set_check_value(True)
			
	def return_book(self, title):
		for book in self._books:
			if book.title == title:
				book.set_check_value(False)
				
	def list_available_books(self):
		for book in self._books:
			if book.is_available() == False:
				print(f"{book.title} by {book.author}")

