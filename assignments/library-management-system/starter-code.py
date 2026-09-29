class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display_info(self):
        # Exiba título, autor, ISBN e disponibilidade
        pass


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def add_borrowed_book(self, book):
        # Adicione o livro à lista de livros emprestados
        pass

    def display_borrowed_books(self):
        # Mostre os títulos dos livros emprestados
        pass


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        # Adicione um livro à biblioteca
        pass

    def add_member(self, member):
        # Registre um novo membro
        pass

    def borrow_book(self, member, book):
        # Verifique se o livro está disponível e faça o empréstimo
        pass


# Exemplo de uso
# library = Library()
# library.add_book(Book("Python Basics", "Alice", "12345"))
# library.add_member(Member("Bob", "M001"))
# library.borrow_book(library.members[0], library.books[0])
