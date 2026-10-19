class Publication:

  def __init__(self, title, author):
    self._title = title
    self._author = author

  def get_title(self):
    return self._title

  def set_title(self, title):
    self._title = title

  def get_author(self):
    return self._author

  def set_author(self, author):
    self._author = author

  def display_info(self):
    return f"Publication Title: {self._title}, Author: {self._author}"


class Book(Publication):

  def __init__(self, title, author, number_of_pages):
    super().__init__(title, author)
    self.set_number_of_pages(number_of_pages)

  def get_number_of_pages(self):
    return self._number_of_pages

  def set_number_of_pages(self, number_of_pages):
    if number_of_pages <= 0:
      print("The number of pages must be positive.")
      self._number_of_pages = None
    else:
      self._number_of_pages = number_of_pages

  def display_info(self):
    return (
        f"Book Title: {self.get_title()}, Author:"
        f" {self.get_author()}, Pages: {self.get_number_of_pages()}"
    )


class Magazine(Publication):

  def __init__(self, title, author, issue_number):
    super().__init__(title, author)
    self.set_issue_number(issue_number)

  def get_issue_number(self):
    return self._issue_number

  def set_issue_number(self, issue_number):
    if issue_number <= 0:
      print("The issue number must be positive.")
      self._issue_number = None
    else:
      self._issue_number = issue_number

  def display_info(self):
    return (
        f"Magazine Title: {self.get_title()}, Author:"
        f" {self.get_author()}, Issue Number:"
        f" {self.get_number() if hasattr(self, 'get_number') else self.get_issue_number()}"
    )

print("=== LIBRARY MANAGEMENT SYSTEM ===\n")

print("--- Publications ---")
pub1 = Publication("General Guidelines", "School Admin")
pub2 = Publication("Student Handbook", "Principal's Office")
print(pub1.display_info())
print(pub2.display_info())

print("\n--- Books ---")
book1 = Book("Python Programming Basics", "John Smith", 280)
book2 = Book("Data Structures and Algorithms", "Jane Doe", 450)
print(book1.display_info())
print(book2.display_info())

print("\n--- Magazines ---")
mag1 = Magazine("Tech Innovators", "Tech Media Group", 42)
mag2 = Magazine("Science Monthly", "Global Science Society", 15)
print(mag1.display_info())
print(mag2.display_info())

print("\n--- Testing Data Validation ---")
invalid_book = Book("Faulty Book", "Unknown Author", -50)
invalid_mag = Magazine("Faulty Magazine", "Unknown Publisher", 0)