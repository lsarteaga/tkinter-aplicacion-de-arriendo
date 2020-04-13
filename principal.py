#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:00:31 2020

@author: lsarteaga
"""
#importaciones
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import logica
import sqlite3

class Aplicacion:
    def __init__(self):
        self.logica = logica.Logica()
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('Arriendos')
        self.notebook = ttk.Notebook(self.ventana_principal)
        self.agregar_inquilino()
        self.listado_inquilinos()
        self.notebook.grid(column = 0, row = 0, padx = 10, pady = 10)
        self.ventana_principal.mainloop()
        
    def agregar_inquilino(self):
        pass
    
    def listado_inquilinos(self):
        pass
    
    def cobrar_arriendo(self):
        pass
    

app = Aplicacion()

