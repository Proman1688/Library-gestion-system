import datetime

class Multa():

    def __init__(self, value):
        self.value = value

    def createFines(self, prestamos=None, value=0):
        today = datetime.date.today()
        value = self.value
        overdueFines = []
        if prestamos is not None:
            for prestamo in prestamos:
                fechaFinal = prestamo.innerFechaFin
                if today > fechaFinal:
                    # calculate the fine based on the number of days overdue
                    daysOverdue = (today - fechaFinal).days
                    value = daysOverdue*self.value  # adjust the 'multa' value amount

                    # create a object for saving the fine
                    class fine:

                        def __init__(self, innerUser, innerBook, fineValue = 0):
                            self.innerUser = innerUser
                            self.innerBook = innerBook
                            self.fineValue = fineValue

                        def __str__(self):
                            return f"------------ Multa info ----------------\n\nLibro: {self.innerBook} \nUsuario: {self.innerUser} \nValor de la multa: {self.fineValue}\n\n---------------- Aqui termina la informacion de la multa --------------------\n\n"

                    Fine = fine(prestamo.innerUser, prestamo.innerBook, value)
                    overdueFines.append(Fine)
                    prestamo.innerBook.disponibilidad = "perdido"

            return overdueFines
        return None
    
    def notifyUsers(self, prestamos = None):
        print("---------------------------- Notified users with fines ----------------\n")
        # list of overdue fines
        overdueFines = self.createFines(prestamos)

        # dictionary to track fines per user
        finesPerUser = {}
        if overdueFines is not None:
            for fine in overdueFines:
                user = fine.innerUser
                fineValue = fine.fineValue

                if user in finesPerUser:
                    finesPerUser[user] += fineValue
                else:
                    finesPerUser[user] = fineValue

            # Send notifications to users with pending fines
            for user, totalFine in finesPerUser.items():
                print(f"Notificacion a {user.nombre}: tienes una multa pendiente de ${totalFine}. por favor paga a tiempo.\n")
        return f"---------------------------- Aqui termina la notificacion de los usuarios con multas ----------------\n\n"

    def listFines(self, prestamos = None):
        overdueFines = self.createFines(prestamos)
        print(f"------ Informacion de las multas ------\n")
        if overdueFines is not None:
            for fine in self.createFines(prestamos):
                print(fine)

        return f"------ Aqui termina la informacion de las multas ------\n\n"
    
    def confirmPayment(self, ISBN, UserId, pay = 0, prestamos = None):
        overdueFines = self.createFines(prestamos)
        if overdueFines is not None and ISBN is not None and UserId is not None:
            for fine in overdueFines:
                if fine.fineValue <= pay and fine.innerUser.getId() == UserId and fine.innerBook.getISBN() == ISBN:
                    overdueFines.remove(fine)
                    return True
            return False
        return None

