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
from tkinter import scrolledtext as st
import logica

class Aplicacion:
    def __init__(self):
        self.logica = logica.Logica() 
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('Arriendos')
        self.ventana_principal.resizable(False, False)
        self.notebook = ttk.Notebook(self.ventana_principal)
        self.primera_pagina()
        self.segunda_pagina()
        self.tercera_pagina()
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
        ttk.Button(self.pagina2, text = 'Mostrar Registros', command = self.obtener_inquilinos).grid(column = 0, row = 0, padx = 4, pady = 4, columnspan = 3, sticky ='we')
        
        #creacion de tabla
        self.tree = ttk.Treeview(self.pagina2, columns = (1,2,3), show = 'headings', height = '5')
        self.tree.grid(column = 0, row = 2, padx = 4, pady = 5, columnspan = 3, sticky = 'we')
        self.tree.heading(1, text = 'Nombre')
        self.tree.heading(2, text = 'Cedula')
        self.tree.heading(3, text = 'Celular')
        ttk.Button(self.pagina2, text = 'Modificar Registro', command = self.modificar_inquilino).grid(column = 1, row = 3, columnspan = 1, sticky = 'we')
        ttk.Button(self.pagina2, text = 'Eliminar Registro', command = self.eliminar_inquilino).grid(column = 2, row = 3, columnspan = 1, sticky = 'ew')
    
    def tercera_pagina(self):
        self.pagina3 = ttk.Frame(self.notebook)
        self.notebook.add(self.pagina3, text = 'Cobrar Arriendo')
        ttk.Label(self.pagina3, text = '').grid(column = 0, row = 0, padx = 4, pady = 4)
        ttk.Label(self.pagina3, text = '').grid(column = 1, row = 0, padx = 4, pady = 4)
        ttk.Label(self.pagina3, text = '').grid(column = 2, row = 0, padx = 4, pady = 4)
        #boton para mostrar inquilinos
        btn1 = tk.Button(self.pagina3, text = 'ACTUALIZAR REGISTROS', command = self.insertar_nombres, fg = 'red')
        btn1.grid(column = 0, row = 0, padx = 4, pady = 4, columnspan = 3, sticky ='we')
        #creacion de la tabla
        self.tree2 = ttk.Treeview(self.pagina3, columns = (1,2,3), show = 'headings', height = '5')
        self.tree2.grid(column = 0, row = 2, padx = 4, pady = 5, columnspan = 3, sticky = 'we')
        self.tree2.heading(1, text = 'Nombre')
        self.tree2.heading(2, text = 'Cedula')
        self.tree2.heading(3, text = 'Celular')
        
       
        #botones para cobrar y mostrar detalle de pago
        ttk.Button(self.pagina3, text = 'Cobrar', command = self.cobrar).grid(column = 1, row = 3, padx = 4, pady = 4, sticky = 'we')
        ttk.Button(self.pagina3, text = 'Detalle', command = self.detalle).grid(column = 2, row = 3, padx = 4, pady = 4, sticky = 'we')
        
        #combo box para seleccionar meses
        self.opcion_seleccionada = tk.StringVar()
        lista = self.obtener_meses()
        self.combo_box = ttk.Combobox(self.pagina3, textvariable = self.opcion_seleccionada, values = lista, state = 'readonly')
        self.combo_box.current(0)
        self.combo_box.grid(column = 0, row = 3, padx = 4, pady = 4, sticky ='we')
    
    def modificar_inquilino(self):
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            mb.showwarning('Atencion', 'Debe seleccionar un registro')
            return
        self.datos_antiguos = self.tree.item(self.tree.selection())['values']
        #creacion de la ventana para actualizar datos
        self.dialogo = tk.Toplevel(self.pagina2)
        self.dialogo.title('Modificacion de Registro')
        self.dialogo.resizable(False, False)
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
            
    def insertar_nombres(self):
        #limpieza de datos al pulsar el boton
        records = self.tree2.get_children()
        for element in records:
            self.tree2.delete(element)
        #obtencion de los datos 
        rows = self.logica.obtener()
        for row in rows:
            self.tree2.insert('', 'end', values = row)
                
    def obtener_meses(self):
        #retorna una lista con los 12 meses
        elementos = self.logica.obtener_arriendos()
        meses = []
        for item in elementos:
            meses.append(item[1])
        return meses
    
    def cobrar(self):
        
        
        try:
            self.tree2.item(self.tree2.selection())['values'][0]
        except IndexError as e:
            mb.showwarning('Atencion', 'SELECCIONE REGISTRO')
            return
        print('opcion combo box ',self.opcion_seleccionada.get())
        #obtencion los datos en la fila seleccionada
        dato_fila = self.tree2.item(self.tree2.selection())['values']
        print('dato fila', dato_fila[0])
        #verificando si el nombre seleccionado existe en la base de datos
        name = self.logica.verificar_existencia((dato_fila[0], ))
        print('nombre',name)
        if name == None:
            mb.showerror('ERROR','ACTUALICE REGISTROS')
        
        else:
            datos = (name[0], self.opcion_seleccionada.get())
            print(datos)
            #obteniendo solo los id de los campos seleccionados
            identificadores = self.logica.obtener_ids(datos)
            print('identificadores',identificadores)
            id_inquilino = self.logica.id_inquilino((dato_fila[0], ))
            print('id inquilino: ', id_inquilino)
            print(id_inquilino[0])
            
            #identificadores es una lista de tuplas [(id_mes, ), (id_inquilino, )]
            idmes_idinq = (identificadores[1][0], id_inquilino[0])
            print(idmes_idinq)
            #se realiza un registro en la base de datos
            self.logica.realizar_cobro(idmes_idinq)
            mb.showinfo('Informacion','Cobro Realizado')
            
            #pinso hacer busqueda individuales
            
       
    #posible eliminacion
    def validar_seleccion(self):
        try:
            self.tree2.item(self.tree2.selection())['values'][0]
        except IndexError as e:
            mb.showwarning('Atencion', 'SELECCIONE REGISTRO')
            return
    
    def detalle(self):
        try:
            self.tree2.item(self.tree2.selection())['values'][0]
        except IndexError as e:
            mb.showwarning('Atencion', 'SELECCIONE REGISTRO')
            return
        
        try:  
           #obtencion de los datos en la fila seleccionada
           dato_fila = self.tree2.item(self.tree2.selection())['values']
           #verficando si el nombre existe en la base de datos
           name = self.logica.verificar_existencia((dato_fila[0], ))      
           if name == None:
               mb.showerror('ERROR','ACTUALICE REGISTROS')
           else:
               self.id_inquilino = ''
               self.id_inquilino = self.logica.id_inquilino(name)
               pagos_inquilino = self.logica.obtener_pagos(self.id_inquilino)
               #la longitud de la lista indica si hay cobros realizados
               if len(pagos_inquilino) == 0:
                   mb.showinfo('Informacion','El inquilino aun no realiza pagos')
               else:
                   #insercion de una nueva ventana para mostrar textos
                   self.dialogo2 = tk.Toplevel(self.pagina3)
                   self.dialogo2.title('Detalle de pagos')
                   self.dialogo2.resizable(False, False)
                   self.dialogo2.protocol("WM_DELETE_WINDOW")        
                   self.dialogo2.grab_set()
                   #implementacion de labels y scroll
                   ttk.Label(self.dialogo2, text = 'Nombre: ').grid(column = 0, row = 0, padx = 4, pady = 4)
                   nombre_inquilino = tk.StringVar()
                   nombre_inquilino.set(dato_fila[0])
                   tk.Entry(self.dialogo2, textvariable = nombre_inquilino, state = 'readonly').grid(column = 1, row = 0, padx = 4, pady = 4)
                   ttk.Label(self.dialogo2, text = 'Cedula: ').grid(column = 0, row = 1, padx = 4, pady = 4)
                   cedula_inquilino = tk.StringVar()
                   cedula_inquilino.set(dato_fila[1])
                   tk.Entry(self.dialogo2, textvariable = cedula_inquilino, state = 'readonly').grid(column = 1, row = 1, padx = 4, pady = 4)
                   ttk.Label(self.dialogo2, text = 'Celular: ').grid(column = 0, row = 2, padx = 4, pady = 4)
                   celular_inquilino = tk.StringVar()
                   celular_inquilino.set(dato_fila[2])
                   tk.Entry(self.dialogo2, textvariable = celular_inquilino, state = 'readonly').grid(column = 1, row = 2, padx = 4, pady = 4)
                   #boton para mostrar el detalle en el scroll text
                   ttk.Button(self.dialogo2, text = 'Mostrar Detalle', command = self.llenar_scroll).grid(column = 0, row = 3, columnspan = 2, sticky = 'we', padx = 4, pady = 10)
                   
                   self.scrolledtext1 = st.ScrolledText(self.dialogo2, width = 30, height = 10)
                   self.scrolledtext1.grid(column = 0, row = 4, padx = 10, pady = 10, columnspan = 2, sticky = 'we')
                   #orden de la consulta (codigo, id_arriendo, id_inquilino)          
        except Exception:
            pass
                
        
    def llenar_scroll(self):
        
        self.scrolledtext1.delete("1.0", tk.END)
        #obtencion de codigo y mes referente al cobro
        elementos = self.logica.datos_scroll(self.id_inquilino)
        for item in elementos:
            print(item)
            self.scrolledtext1.insert(tk.END,'Codigo de cobro: ' + str(item[0]) + '\nMes Pagado: ' + str(item[1]) + '\n\n')
            
        
    
app = Aplicacion()

