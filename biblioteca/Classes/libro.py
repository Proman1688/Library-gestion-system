# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:31:14 2023

@author: JUANCHO 
"""

class Libro:
    
# Codigo para el constructor
    def __init__(self, titulo=None, autor=None, genero=None, ISBN=None, num_copias=None, disponibilidad="disponible", categoria=None):
        
        self.titulo = titulo
        self.autor= autor
        self.genero= genero
        self.ISBN= ISBN
        self. num_copias = num_copias if num_copias is not None else 0
        self.disponibilidad = disponibilidad
        self.categoria = categoria
        self.prestamosTotales = 0

    def __str__(self):
        return f"Titulo: {self.titulo} \nAutor: {self.autor} \nGenero: {self.genero} \nISBN: {self.ISBN} \nNumero de copias: {self.num_copias} \nDisponibilidad: {self.disponibilidad}\nPrestamos: {self.prestamosTotales} \n\n"
    
    def getTitulo (self):
        return self.titulo
    
    def getAutor (self):
        return self.autor

    def getGenero (self):
        return self.genero
    
    def getISBN (self):
        return self.ISBN 
        
    
    