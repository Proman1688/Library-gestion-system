from Classes.multa import Multa
import datetime

class Prestamo(): 

    def __init__(self, value=0):
        self.prestamos = [] 
        self.multa = Multa(value)

    def share(self, book, user, dias, day = None, month = None, year = None):
        self.book = book
        self.user = user

        if book is not None and user is not None and book.num_copias > 0:
            book.num_copias -= 1
            self.fechaInicio = datetime.date.today() if year is None else datetime.date(year, month, day)
            self.fechaFin = self.fechaInicio + datetime.timedelta(days=dias)
            
            #subclase de prestamo que crea los objetos prestamo que luego vamos a encapsular
            class prestamoSub:

                def __init__(self, innerBook, innerUser, innerFechaInicio, innerFechaFin):
                    self.innerBook = innerBook
                    self.innerUser = innerUser
                    self.innerFechaInicio = innerFechaInicio
                    self.innerFechaFin = innerFechaFin

                def __str__(self):
                    return f"------------ Prestamo info ----------------\n\nLibro: {self.innerBook} \nUsuario: {self.innerUser} \nFecha de inicio: {self.innerFechaInicio} \nFecha de fin: {self.innerFechaFin}\n\n---------------- Aqui termina la informacion del prestamo --------------------\n\n"

            prestamo = prestamoSub(book, user, self.fechaInicio, self.fechaFin)
            self.prestamos.append(prestamo)

            if book.num_copias == 0:
                book.disponibilidad = "prestados"

            return book.num_copias
        else:
            return False
    
    def confirmPay(self, pay, ISBN = None, userId = None): 
        check = self.multa.confirmPayment(ISBN, userId, pay, self.prestamos) #retorna True si el pago se realizo, False si no se realizo, None si no hay multas
        if check is True: # Check if the payment was confirmed
            return True
        if check is False: # Check if the payment was not confirmed
            return f"Error al confirmar el pago (verificar el id del usuario, el ISBN o el monto del pago)\n"
        else:
            return f"No hay multas pendientes\n"
        
    def devolver(self, ISBN, UserId):
        if input("Esta seguro que desea continuar? s/n") == 'n':
            return None
        check = self.multa.createFines(self.prestamos, self.multa.value) # check is the list o fines
        if check is not None: #check is None if there are no fines
            for multa in check: 
                if multa.innerBook.getISBN() == ISBN and multa.innerUser.getId() == UserId: #busca la multa en caso de haberla del prestamo a devolver
                    check2 = input(f"El usuario {multa.innerUser.getNombre()} tiene una multa pendiente de ${multa.fineValue}. Realizar pago? s/n.\n") # alert that the user has an unpaid fine
                    if check2.lower() == 's':
                        check2 = self.confirmPay(int(input("\ningrese el valor a pagar: ")), ISBN, UserId) # check2 is True if the payment was confirmed, False if not
                        print(f"\n{check2}\n")
                        if check2 is True: # the fine has been removed so as well the share
                            for prestamo in self.prestamos:
                                if (prestamo.innerBook.getISBN() == ISBN and prestamo.innerUser.getId() == UserId): # remove the share from the list if it exist
                                    self.prestamos.remove(prestamo)
                                    # Update book availability and copy count
                                    prestamo.innerBook.num_copias += 1
                                    if prestamo.innerBook.num_copias > 0:
                                        prestamo.innerBook.disponibilidad = "disponible"
                                    return prestamo.innerBook.num_copias
                            return False
                    if check2.lower() == 'n':
                        return False
                    else:
                        return None
        for prestamo in self.prestamos:
            if (prestamo.innerBook.getISBN() == ISBN and prestamo.innerUser.getId() == UserId):
                self.prestamos.remove(prestamo)
                # Update book availability and copy count
                prestamo.innerBook.num_copias += 1
                if prestamo.innerBook.num_copias > 0:
                    prestamo.innerBook.disponibilidad = "disponible"
                return prestamo.innerBook.num_copias
        return False
    
    def listPrestamos(self):
        print(f"------ Informacion de los prestamos ------\n")
        for prestamo in self.prestamos:
            print(prestamo)
        return f"------ Aqui termina la informacion de los prestamos ------\n\n"
    