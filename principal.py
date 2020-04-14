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
        self.pagina_agregar = ttk.Frame(self.notebook)
        self.notebook.add(self.pagina_agregar, text = 'Agregar Inquilino')
        self.label_frame = ttk.Labelframe(self.pagina_agregar, text = 'Datos inquilino')
        self.label_frame.grid(column = 0, row = 0, padx = 5, pady = 10)
        #labels y entrys para ingreso de datos
        ttk.Label(self.label_frame, text = 'Nombre: ').grid(column = 0, row = 0, padx = 4, pady = 4)
        self.nombre_inquilino =tk.StringVar()
        ttk.Entry(self.label_frame, textvariable = self.nombre_inquilino).grid(column = 1, row = 0, padx = 4, pady = 4)
        ttk.Label(self.label_frame, text = 'Cedula: ').grid(column = 0, row = 1, padx = 4, pady = 4)
        self.cedula_inquilino =tk.StringVar()
        ttk.Entry(self.label_frame, textvariable = self.cedula_inquilino).grid(column = 1, row = 1, padx = 4, pady = 4)
        ttk.Label(self.label_frame, text = 'Celular: ').grid(column = 0, row = 2, padx = 4, pady = 4)
        self.celular_inquilino =tk.StringVar()
        ttk.Entry(self.label_frame, textvariable = self.celular_inquilino).grid(column = 1, row = 2, padx = 4, pady = 4)
        #boton para agregar
        ttk.Button(self.label_frame, text = 'Agregar').grid(column = 0, row = 3, columnspan = 2, sticky = 'we', padx = 4, pady = 10)
    
    def listado_inquilinos(self):
        pass
    
    def cobrar_arriendo(self):
        pass
    

app = Aplicacion()

