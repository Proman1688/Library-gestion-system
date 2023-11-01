from Classes.usuario import Usuario 

class UserControl:
    
    def __init__(self): #encapsulamiento de los usuarios
        self.users = []

    def getUser(self, identificacion):
        for user in self.users:
            if user is not None and user.getId() == identificacion:
                return user
        return None
    
    def addUser(self, nombre=None, identificacion=None, correo=None, telefono=None):
        usuario = Usuario(nombre, identificacion, correo, telefono)
        self.users.append(usuario)

    def editUser(self, identificacion, newId=None, newNombre=None, newCorreo=None, newTelefono=None):
        if input("Esta seguro que desea continuar? s/n") == 'n':
            return f"The changes were not made"
        for user in self.users:
            if user is not None and user.getId() == identificacion:
                if newId is not None:
                    user.identificacion = newId
                if newNombre is not None:
                    user.nombre = newNombre
                if newCorreo is not None:
                    user.correo = newCorreo
                if newTelefono is not None:
                    user.telefono = newTelefono
                return f"the user information was successfully updated"
        return f"The user {identificacion} was not found"
    
    def deleteUser(self, identificacion):
        if input("Esta seguro que desea continuar? s/n") == 'n':
            return f"The changes were not made"
        for user in self.users:
            if user is not None and user.getId() == identificacion:
                self.users.remove(user)
                return f"the user information was successfully deleted"
        return f"The user {identificacion} was not found"
    
    def searchUser(self, criterio, value = None):
        print(f"------ Informacion de los usuarios encontrados con el valor {value} ------\n")
        check = 0
        for user in self.users:
            if criterio == 1:
                if user is not None and user.getId() == value:
                    print(user)
                    check = 1
            if criterio == 2:
                if user is not None and user.getNombre() == value:
                    print(user)
                    check = 1
            if criterio == 3:
                if user is not None and user.getTelefono() == value:
                    print(user)
                    check = 1
            if criterio == 4:
                if user is not None and user.getCorreo() == value:
                    print(user)
                    check = 1
        if check == 0:
            return f"No se enontro el usuario con la informacion: {value}\n\n"
        else:
            return f"------ Aqui termina la informacion de los usuarios encontrados ------\n\n"
        
    def addStatistic(self, Id):
        for user in self.users:
            if user is not None and user.getId() == Id:
                user.prestamosTotales += 1

        
    def listUsers(self):
        print("------ Informacion de los usuarios ------\n")
        for user in self.users:
            if user is not None:
                print(user)
        print("------ Aqui termina la informacion de los usuarios ------\n\n")