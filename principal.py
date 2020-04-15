#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:00:31 2020

@author: lsarteaga
"""
#importaciones
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import logica

class Aplicacion:
    def __init__(self):
        self.logica = logica.Logica()
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('Arriendos')
        self.notebook = ttk.Notebook(self.ventana_principal)
        self.primera_pagina()
        self.segunda_pagina()
        self.notebook.grid(column = 0, row = 0, padx = 10, pady = 10)
        self.ventana_principal.mainloop()
        
    def primera_pagina(self):
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
        ttk.Button(self.label_frame, text = 'Agregar', command = self.validacion_datos).grid(column = 0, row = 3, columnspan = 2, sticky = 'we', padx = 4, pady = 10)
    
    def segunda_pagina(self):

        self.pagina2 = ttk.Frame(self.notebook)
        self.notebook.add(self.pagina2, text = 'Listado de Inquilinos')
        ttk.Label(self.pagina2, text = '').grid(column = 0, row = 0, padx = 4, pady = 4)
        ttk.Label(self.pagina2, text = '').grid(column = 1, row = 0, padx = 4, pady = 4)
        ttk.Label(self.pagina2, text = '').grid(column = 2, row = 0, padx = 4, pady = 4)

        #creacion de boton 
        ttk.Button(self.pagina2, text = 'Actualizar Registros', command = self.obtener_inquilinos).grid(column = 0, row = 0, padx = 4, pady = 4, columnspan = 3, sticky ='we')
        
        #creacion de tabla
        self.tree = ttk.Treeview(self.pagina2, columns = (1,2,3), show = 'headings', height = '5')
        self.tree.grid(column = 0, row = 2, padx = 4, pady = 5, columnspan = 3, sticky = 'we')
        self.tree.heading(1, text = 'Nombre')
        self.tree.heading(2, text = 'Cedula')
        self.tree.heading(3, text = 'Celular')
        ttk.Button(self.pagina2, text = 'Modificar Registro', command = self.modificar_inquilino).grid(column = 1, row = 3, columnspan = 1, sticky = 'we')
        ttk.Button(self.pagina2, text = 'Eliminar Registro', command = self.eliminar_inquilino).grid(column = 2, row = 3, columnspan = 1, sticky = 'ew')
        
    def modificar_inquilino(self):
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            mb.showwarning('Atencion', 'Debe seleccionar un registro')
            return
        self.datos_antiguos = self.tree.item(self.tree.selection())['values']
        #creacion de la ventana para actualizar datos
        self.dialogo = tk.Toplevel(self.pagina2)
        ttk.Label(self.dialogo, text = 'NUEVO NOMBRE: ').grid(column = 0, row = 0, padx = 4, pady = 4)
        ttk.Entry(self.dialogo, textvariable = self.nombre_inquilino).grid(column = 1, row = 0, padx = 4, pady = 4)
        ttk.Label(self.dialogo, text = 'NUEVA CEDULA: ').grid(column = 0, row = 1, padx = 4, pady = 4)
        ttk.Entry(self.dialogo, textvariable = self.cedula_inquilino).grid(column = 1, row = 1, padx = 4, pady = 4)
        ttk.Label(self.dialogo, text = 'NUEVO CELULAR: ').grid(column = 0, row = 2, padx = 4, pady = 4)
        ttk.Entry(self.dialogo, textvariable = self.celular_inquilino).grid(column = 1, row = 2, padx = 4, pady = 4)
        ttk.Button(self.dialogo, text = 'ACTUALIZAR', command = self.verificar_dialogo).grid(column = 0, row = 3, padx = 4, pady = 4, columnspan = 2, sticky = 'we')
        self.dialogo.protocol("WM_DELETE_WINDOW")        
        self.dialogo.grab_set()
      
    def actualizar_datos(self):
        self.datos_actualizados = (self.nombre_inquilino.get(), self.cedula_inquilino.get(), self.celular_inquilino.get(), self.datos_antiguos[0])
        self.logica.actualizar(self.datos_actualizados)
        mb.showinfo('Informacion','Registro actualizado')
        self.dialogo.destroy()
        datos_muestra = (self.nombre_inquilino.get(), self.cedula_inquilino.get(), self.celular_inquilino.get())
        self.nombre_inquilino.set('')
        self.cedula_inquilino.set('')
        self.celular_inquilino.set('')
        #se obtiene la posicion de la fila seleccionada en la tabla
        #se elimina dicha fila
        #se ingresa al final de la tabla una nueva fila con los datos actualizados usando la variable 'datos_muestra'
        #al pulsar ACTUALIZAR las filas modificadas recuperan su posicion 
        item = self.tree.selection()
        self.tree.delete(item)
        self.tree.insert('', 'end' ,values = datos_muestra)
        
    def verificar_dialogo(self):
        if self.nombre_inquilino.get() == '' or self.cedula_inquilino.get() == '' or self.celular_inquilino.get() == '':
            mb.showwarning('Atencion','Debe llenar todos los campos')
        else:
            self.actualizar_datos()    

    def eliminar_inquilino(self):
        
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            mb.showwarning('Atencion', 'Debe seleccionar un registro')
            return
        #aqui retorna una tupla de todos los campos (nombre,cedula,celular)
        valor = self.tree.item(self.tree.selection())['values']
        self.logica.eliminar(valor[0])
        mb.showinfo('Informacion','Registro eliminado')
        #para eliminar el registro de la tabla
        item = self.tree.selection()
        self.tree.delete(item)
    
    def agregar_inquilino(self):
        
        datos_inquilino = (self.nombre_inquilino.get(), self.cedula_inquilino.get(), self.celular_inquilino.get())
        self.logica.agregar(datos_inquilino)
        mb.showinfo('Informacion', 'Registro exitoso')
        #vaciando los campos de entrada
        self.nombre_inquilino.set('')
        self.cedula_inquilino.set('')
        self.celular_inquilino.set('')
        
        
    def validacion_datos(self):
        if self.nombre_inquilino.get() == '' or self.cedula_inquilino.get() == '' or self.celular_inquilino.get() == '':
            mb.showwarning('Atencion','Debe llenar todos los campos')
        else:
            self.agregar_inquilino()
    
    def obtener_inquilinos(self):
        self.limpiar_tabla()
        rows = self.logica.obtener()
        for row in rows:
            self.tree.insert('', 'end', values = row)
            
    def limpiar_tabla(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
            

app = Aplicacion()

