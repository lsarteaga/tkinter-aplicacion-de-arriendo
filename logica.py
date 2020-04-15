#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:43:10 2020

@author: lsarteaga
"""
#importaciones
import sqlite3

class Logica:
    def establecer_conexion(self):
        conexion = sqlite3.connect('arriendo.db')
        return conexion
    
    def agregar(self, datos_inquilino):
        cone = self.establecer_conexion()
        cursor = cone.cursor()
        sql = 'INSERT INTO inquilinos (nombre, cedula, celular) VALUES (?,?,?)'
        cursor.execute(sql, datos_inquilino)
        cone.commit()
        cone.close()
        
    def obtener(self):
        try:
            cone = self.establecer_conexion()
            cursor = cone.cursor()
            sql = 'SELECT nombre,cedula,celular FROM inquilinos'
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close
        
    def eliminar(self, valor):
        cone = self.establecer_conexion()
        cursor = cone.cursor()
        sql = 'DELETE FROM inquilinos WHERE nombre = ?'
        cursor.execute(sql, (valor, ))
        cone.commit()
        cone.close()
    
    def actualizar(self, datos_actualizados):
        cone = self.establecer_conexion()
        cursor = cone.cursor()
        sql = 'UPDATE inquilinos SET nombre = ?, cedula = ?, celular = ? WHERE nombre = ?'
        cursor.execute(sql, datos_actualizados)
        cone.commit()
        cone.close()
        
    #creando nuevas tablas y relacionandolas
    def cambios_db(self):
        cone = self.establecer_conexion()
        cursor = cone.cursor()
        command1 = """CREATE TABLE IF NOT EXISTS 
        arriendos(id_arriendo INTEGER PRIMARY KEY AUTOINCREMENT, mes TEXT NOT NULL,
        estado TEXT NOT NULL)"""
        cursor.execute(command1)
        command2 = """CREATE TABLE IF NOT EXISTS inquilino_arriendo(codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        id_arriendo INTEGER REFERENCES arriendos(id_arriendo) ON DELETE CASCADE ON UPDATE CASCADE,
        id_inquilino INTEGER REFERENCES inquilinos(id_inquilino) ON DELETE CASCADE ON UPDATE CASCADE)"""
        cursor.execute(command2)
        cone.commit()
        cone.close()
    
        
        
        
        
        

