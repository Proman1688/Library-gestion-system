# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 08:57:34 2023
 
@author: JUANCHO
"""

class Usuario:
    
# Codigo para el constructor
    def __init__(self, nombre, identificacion, correo, telefono):
        
        self.nombre = nombre
        self.identificacion= identificacion
        self.correo= correo
        self.telefono= telefono if telefono is not None else None
        self.prestamosTotales = 0

    def __str__(self):
        return f"Nombre: {self.nombre} \nId: {self.identificacion} \nCorreo: {self.correo} \nTelefono: {self.telefono}\nPrestamos: {self.prestamosTotales} \n\n"
    
    def getId(self):
        return self.identificacion
    
    def getCorreo(self):
        return self.correo

    def getTelefono(self):
        return self.telefono
    
    def getNombre(self):
        return self.nombre
    
  #realizar operacion modificar usuario
  
    