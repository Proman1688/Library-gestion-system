from Classes.libro import Libro
from Classes.prestamo import Prestamo
from Classes.category import Category

class BookManagment: 
 
    def __init__(self): 
        self.books = [] #encapsulamiento de los libros
        self.categories = [] # encapsulamiento de categorias

    def getBook(self, ISBN):
        for book in self.books:
            if book is not None and book.getISBN() == ISBN:
                return book

    # add new book
    def addBook(self, titulo=None, autor=None, genero=None, ISBN=None, num_copias=None, disponibilidad="disponible", category=None):
        libro = Libro(titulo, autor, genero, ISBN, num_copias, disponibilidad, category) #instancio nuevo objeto
        self.books.append(libro)

    #search a book
    def searchBook(self, criterio, value = None):
        print(f"------ Informacion de los libros encontrados con el valor {value} ------\n")
        check = 0
        for book in self.books:
            if criterio == 1:
                if book is not None and (book.getTitulo() != None and book.getTitulo().lower() == value.lower()):
                    print(book)
                    check = 1
            if criterio == 2:
                if book is not None and (book.getAutor() != None and book.getAutor().lower() == value.lower()):
                    print(book)
                    check = 1
            if criterio == 3:
                if book is not None and (book.getGenero() != None and book.getGenero().lower() == value.lower()):
                    print(book)
                    check = 1
        if check == 0:
            return f"No se enontro el libro con la informacion: {value}\n\n"
        else:
            return f"------ Aqui termina la informacion de los libros encontrados ------\n\n"
    
    #delete a book by its ISBN
    def deleteBookByISBN(self, ISBN=None):
        if input("Esta seguro que desea continuar? s/n") == 'n':
            return f"The changes were not made"
        for book in self.books:
            if book is not None and (book.getISBN() != None and book.getISBN().lower() == ISBN.lower()):
                self.books.remove(book)
                return f"the book was succesfully deleted"
        return f"the book with the ISBN {ISBN} was not found\n"
    
    def listBooks(self):
        print(f"------ Informacion de los libros ------\n")
        for book in self.books:
            if book is not None:
                print(book)
        return f"------ Aqui termina la informacion de los libros ------\n\n"

    # ------------------------------ Category management ------------------------------

    def addCategory(self, name, parent=None):
        category = Category(name, parent) #instancio nuevo objeto category
        if parent is not None:
            parent.addSubCategory(category)
        self.categories.append(category)

    def getSubcategoryCount(self, categoryName):
        category = self.findCategoryByName(categoryName)
        if category:
            return category.getSubCategoriesCount()
        return 0
    
    def findCategoryByName(self, categoryName):
        for category in self.categories:
            if category.name.lower() == categoryName.lower():
                return category
        return None
    
    def seeAllCategories(self, categories):
        print("============================ Categories ============================================\n")
        for categories in self.categories:
            if not categories.parent:
                categories.displayTree()
                print("--------------------------- End of Category Tree -----------------------------------\n")
        print("========================= End of All categories ====================================\n")
        
    
    #=====================================================================================
    
    # ====================================== Inventory management ========================
    
    #Reload the inventory
    def inventory(self, ISBN = None, nuevas_copias = None, share = False):
        for book in self.books:
            if book is not None and (book.getISBN() != None and book.getISBN().lower() == ISBN.lower()):
                book.num_copias = nuevas_copias
                if share is True:
                    book.prestamosTotales += 1
                return f"the inventory was successfully reloaded"
        return f"the book with ISBN {ISBN} was not found"
    
    # =====================================================================================
    
    # instance a prestamo object
    def shareBook(self, value=0):
        return Prestamo(value)