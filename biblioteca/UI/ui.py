import os
from Classes.bookManagment import BookManagment
from Classes.userControl import UserControl

class Ui:
    
    def __init__(self):
        self.bookManager = BookManagment()
        self.userControl = UserControl()
        self.prestamo = self.bookManager.shareBook()

        # ============================================= Create a starting database of users =============
        self.userControl.addUser("Juan", "123", "juan@gmail.com", "1344242") 
        self.userControl.addUser("Maria", "456", "maria@gmail.com", "9876543")
        self.userControl.addUser("Carlos", "789", "carlos@gmail.com", "6543210")
        self.userControl.addUser("Linda", "101", "linda@gmail.com", "2468135")
        self.userControl.addUser("Sophia", "222", "sophia@gmail.com", "5551234")
        self.userControl.addUser("Ethan", "333", "ethan@gmail.com", "8884321")
        self.userControl.addUser("Olivia", "444", "olivia@gmail.com", "1112223")
        self.userControl.addUser("Aiden", "555", "aiden@gmail.com", "7779998")
        self.userControl.addUser("Emma", "666", "emma@gmail.com", "6665555")
        self.userControl.addUser("Liam", "777", "liam@gmail.com", "9996664")
        self.userControl.addUser("Isabella", "888", "isabella@gmail.com", "4441117")
        self.userControl.addUser("Noah", "999", "noah@gmail.com", "3337776")

         # ============================================= Create a starting database of Categories =========
        
        self.bookManager.addCategory("Programming")
        self.bookManager.addCategory("Mathematics")
        self.bookManager.addCategory("Humanities")
        self.bookManager.addCategory("Literature")
        self.bookManager.addCategory("Fiction", parent=self.bookManager.findCategoryByName("Literature"))
        self.bookManager.addCategory("Explosion", parent=self.bookManager.findCategoryByName("Fiction"))
        self.bookManager.addCategory("Tale", parent=self.bookManager.findCategoryByName("Literature"))
        self.bookManager.addCategory("Science")
        self.bookManager.addCategory("Technology", parent=self.bookManager.findCategoryByName("Science"))
        self.bookManager.addCategory("Computer Science", parent=self.bookManager.findCategoryByName("Technology"))
        self.bookManager.addCategory("Physics", parent=self.bookManager.findCategoryByName("Science"))
        self.bookManager.addCategory("Biology", parent=self.bookManager.findCategoryByName("Science"))
        self.bookManager.addCategory("Philosophy")
        self.bookManager.addCategory("History")
        self.bookManager.addCategory("Geography", parent=self.bookManager.findCategoryByName("Humanities"))
        self.bookManager.addCategory("Ancient History", parent=self.bookManager.findCategoryByName("History"))
        self.bookManager.addCategory("Modern History", parent=self.bookManager.findCategoryByName("History"))

        # ============================================= Create a starting database of Books ================

        self.bookManager.addBook("El señor de los anillos", "J.R.R. Tolkien", "Fantasia", "978-84-450-7570-9", 5, category=self.bookManager.findCategoryByName("Literature"))
        self.bookManager.addBook("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy", "978-0439708180", 3, category=self.bookManager.findCategoryByName("Literature"))
        self.bookManager.addBook("To Kill a Mockingbird", "Harper Lee", "Fiction", "978-0061120084", 4, category=self.bookManager.findCategoryByName("Fiction"))
        self.bookManager.addBook("1984", "George Orwell", "Science Fiction", "978-0451524935", 2, category=self.bookManager.findCategoryByName("Fiction"))
        self.bookManager.addBook("The Great Gatsby", "F. Scott Fitzgerald", "Classics", "978-0743273565", 3,category=self.bookManager.findCategoryByName("Humanities"))
        self.bookManager.addBook("Introduction to Algorithms", "Thomas H. Cormen", "Computer Science", "978-0262033848", 5, category=self.bookManager.findCategoryByName("Computer Science"))
        self.bookManager.addBook("The Theory of Everything", "Stephen Hawking", "Physics", "978-8179927930", 3, category=self.bookManager.findCategoryByName("Physics"))
        self.bookManager.addBook("The Origin of Species", "Charles Darwin", "Biology", "978-0199219223", 4, category=self.bookManager.findCategoryByName("Biology"))
        self.bookManager.addBook("Meditations", "Marcus Aurelius", "Philosophy", "978-0679642602", 5, category=self.bookManager.findCategoryByName("Philosophy"))
        self.bookManager.addBook("A Brief History of Time", "Stephen Hawking", "Science", "978-0553380163", 3, category=self.bookManager.findCategoryByName("Science"))
        self.bookManager.addBook("The Republic", "Plato", "Philosophy", "978-0140455113", 4, category=self.bookManager.findCategoryByName("Philosophy"))

        # =============================================== Create some shares =================================

        check = self.prestamo.share(self.bookManager.getBook("978-8179927930"), self.userControl.getUser("333"), 14)
        self.userControl.addStatistic("333")
        self.bookManager.inventory("978-8179927930", check, True)
        check = self.prestamo.share(self.bookManager.getBook("978-8179927930"), self.userControl.getUser("777"), 10)
        self.userControl.addStatistic("777")
        self.bookManager.inventory("978-8179927930", check, True)
        check = self.prestamo.share(self.bookManager.getBook("978-0061120084"), self.userControl.getUser("123"), 7)
        self.userControl.addStatistic("123")
        self.bookManager.inventory("978-0061120084", check, True)
        check = self.prestamo.share(self.bookManager.getBook("978-84-450-7570-9"), self.userControl.getUser("999"), 20)
        self.userControl.addStatistic("999")
        self.bookManager.inventory("978-84-450-7570-9", check, True)
        check = self.prestamo.share(self.bookManager.getBook("978-8179927930"), self.userControl.getUser("666"), 14)
        self.userControl.addStatistic("666")
        self.bookManager.inventory("978-8179927930", check, True)
        check = self.prestamo.share(self.bookManager.getBook("978-0140455113"), self.userControl.getUser("123"), 7)
        self.userControl.addStatistic("123")
        self.bookManager.inventory("978-0140455113", check, True)

        # overdue shares

        check = self.prestamo.share(self.bookManager.getBook("978-0140455113"), self.userControl.getUser("333"), 10, 22, 11, 2022)
        self.userControl.addStatistic("333")
        self.bookManager.inventory("978-0140455113", check, True)
        check = self.prestamo.share(self.bookManager.getBook("978-0262033848"), self.userControl.getUser("101"), 8,  12, 12, 2022)
        self.userControl.addStatistic("101")
        self.bookManager.inventory("978-0262033848", check, True)
        check = self.prestamo.share(self.bookManager.getBook("978-0140455113"), self.userControl.getUser("123"), 7, 18, 10, 2023)
        self.userControl.addStatistic("123")
        self.bookManager.inventory("978-0140455113", check, True)

    def displayMenu(self):
        print("---------------------------------------------")
        print("        Library Management System Menu")
        print("---------------------------------------------\n")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Delete a Book")
        print("4. Inventory Management")
        print("5. Borrow a Book")
        print("6. Return a Book")
        print("7. List All Books")
        print("8. List Borrowed Books")
        print("9. Notify users about fines")
        print("10. List Fines")
        print("11. Add a Category")
        print("12. Know amount of subCategories")
        print("13. See all categories")
        print("14. Add an User")
        print("15. Edit an User")
        print("16. Delete an User")
        print("17. Search an User")
        print("18. List all Users")
        print("19. Statistics")
        print("0. Exit\n")

    def selectSearchCriteria(self):
        print("---------------------------------------------")
        print("        Select a criteria for searching")
        print("---------------------------------------------\n")
        print("1. By title")
        print("2. By author")
        print("3. By genre")
        print("4. Cancel\n")
        check = int(input("Select a criteria: "))
        return check
    
    def selectSearchCriteria2(self):
        print("---------------------------------------------")
        print("        Select a criteria for searching")
        print("---------------------------------------------\n")
        print("1. By Id")
        print("2. By Name")
        print("3. By Phone number")
        print("4. By Email")
        print("5. Cancel\n")
        check = int(input("Select a criteria: "))
        return check
    
    def selectStartDate(self):
        print("---------------------------------------------")
        print("        Select a start date for sharing")
        print("---------------------------------------------\n")
        print("1. Today")
        print("2. Add a date")
        print("3. Cancel\n")
        check = int(input("Select an option: "))
        return check

    def run(self):
        while True:
            os.system('cls')
            self.displayMenu()
            userChoice = input("Please enter your choice (1-19): ")
            os.system('cls')
            
            if userChoice == '1':
                self.bookManager.addBook(input("Enter the title of the book"), input("Enter the author of the book"), input("Enter the genre of the book"), input("Enter the ISBN code of the book"), int(input("Enter the number of book copies")), category=self.bookManager.findCategoryByName(input("Enter the book category (already existing)")))
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '2':
                check = self.selectSearchCriteria()
                if check != 4 or None:
                    print(self.bookManager.searchBook(check, input("enter the information for search: ")))
                    input("\nPress Enter to continue...")
                pass
            elif userChoice == '3':
                print(self.bookManager.deleteBookByISBN(input("Enter the ISBN code of the book")))
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '4':
                ISBN = input("Enter the ISBN code of the book to reload")
                numOfCopies = input("Enter the new number of book copies")
                if numOfCopies is not (None or ''):
                    print(self.bookManager.inventory(ISBN, int(numOfCopies)))
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '5':
                check = self.selectStartDate()
                ISBN = input("Enter the ISBN code of the book")
                Id = input("Enter the id of the user")
                book = self.bookManager.getBook(ISBN)
                user = self.userControl.getUser(Id)
                if check == 1:
                    check1 = self.prestamo.share(book, user, int(input("Enter the time of days the book is going  to be shared: ")))
                    if check1 is False:
                        print("Prestamo Fallido\n")
                    else:
                        print("Prestamo Exitoso\n")
                        self.userControl.addStatistic(user.identificacion)
                        self.bookManager.inventory(ISBN, check1, True)
                    input("\nPress Enter to continue...")
                if check == 2:
                    check1 = self.prestamo.share(book, user, int(input("Enter the time of days the book is going  to be shared: ")), int(input("Enter the day of the date")), int(input("Enter the month of the date")), int(input("Enter the year of the date")))
                    if check1 is False:
                        print("Prestamo Fallido\n")
                    else:
                        print("Prestamo Exitoso\n")
                        self.userControl.addStatistic(user.identificacion)
                        print(self.bookManager.inventory(ISBN, check1, True))
                    input("\nPress Enter to continue...")
                pass
            elif userChoice == '6':
                ISBN = input("Enter the book ISBN: ")
                Id = input("Enter the user Id: ")
                check = self.prestamo.devolver(ISBN, Id)
                if check is False:
                    print("Devolucion Fallida\n")
                else: 
                    if check is None:
                        print("La devolucion no se pudo realizar.\n")
                    else:
                        print(self.bookManager.inventory(ISBN, check))
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '7':
                print(self.bookManager.listBooks())
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '8':
                print(self.prestamo.listPrestamos())
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '9':
                print(self.prestamo.multa.notifyUsers(self.prestamo.prestamos))
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '10':
                print(self.prestamo.multa.listFines(self.prestamo.prestamos))
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '11':
                self.bookManager.addCategory(input("Enter the name of the category: "), input("Enter the name of the parent category (enter if not apply): "))
                pass
            elif userChoice == '12':
                print(self.bookManager.getSubcategoryCount(input("Enter the name of the category: ")))
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '13':
                self.bookManager.seeAllCategories(self.bookManager.categories)
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '14':
                Phone = input("Enter the phone of the user:")
                Id = input("Enter the Id of the user: ")
                self.userControl.addUser(input("Enter the name of the user: "), Id, input("Enter the email of the user: "), Phone)
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '15':
                print(self.userControl.editUser(input("Enter the current user Id's: "), input("Enter the new user Id's: "), input("Enter the new user name: "), input("Enter the new user email: "), input("Enter the new user phone: ")))
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '16':
                print(self.userControl.deleteUser(input("Enter the user Id: ")))
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '17':
                check = self.selectSearchCriteria2()
                if check != 5 or None:
                    print(self.userControl.searchUser(check, input("enter the information for search: ")))
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '18':
                print(self.userControl.listUsers())
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '19':
                print("El libro con mas cantidad de prestamos es:\n")
                print(max(self.bookManager.books, key = lambda book: book.prestamosTotales))
                print("El libro con menos cantidad de prestamos es:\n")
                print(min(self.bookManager.books, key = lambda book: book.prestamosTotales))
                print("El usuario con mas cantidad de prestamos es:\n")
                print(max(self.userControl.users, key = lambda user: user.prestamosTotales))
                print("El usuario con menos cantidad de prestamos es:\n")
                print(min(self.userControl.users, key = lambda user: user.prestamosTotales))
                input("\nPress Enter to continue...")
                pass
            elif userChoice == '0':
                print("Exiting the Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option (1-19).")
            os.system('cls')

