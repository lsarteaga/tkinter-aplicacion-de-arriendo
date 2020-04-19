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
        conexion = sqlite3.connect('/home/lsarteaga/Projects/bases de datos/registros.db')
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
        
    
    #para obtener meses
    def obtener_arriendos(self):
        try:
            conn = self.establecer_conexion()
            cursor = conn.cursor()
            sql = 'SELECT * FROM arriendos'
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            conn.close()
            
    def realizar_cobro(self, idmes_idinq):
        conn = self.establecer_conexion()
        cursor = conn.cursor()
        sql = 'INSERT INTO inquilino_arriendo (id_arriendo, id_inquilino) VALUES (?,?)'
        cursor.execute(sql, idmes_idinq)
        conn.commit()
        conn.close()
        
    def obtener_ids(self, datos):
        try:
            conn = self.establecer_conexion()
            cursor = conn.cursor()
            sql = 'SELECT id_inquilino FROM inquilinos WHERE nombre = ? UNION SELECT id_arriendo FROM arriendos WHERE mes = ?'
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            conn.close()
        
    def verificar_existencia(self, valor):
        try:
            conn = self.establecer_conexion()
            cursor = conn.cursor()
            sql = 'SELECT nombre FROM inquilinos WHERE nombre = ?'
            cursor.execute(sql, valor)
            return cursor.fetchone()
        finally:
            conn.close()
    #EN REVISION!!!
            
    def obtener_pagos(self, id_inquilino):
        try:
            conn = self.establecer_conexion()
            cursor = conn.cursor()
            sql = 'SELECT * FROM inquilino_arriendo WHERE id_inquilino = ?'
            cursor.execute(sql, id_inquilino)
            return cursor.fetchall()
        finally:
            conn.close()
            
    ########
            
    def id_inquilino(self, nombre_inquilino):
        try:
            conn = self.establecer_conexion()
            cursor = conn.cursor()
            sql = 'SELECT id_inquilino FROM inquilinos WHERE nombre = ?'
            cursor.execute(sql, nombre_inquilino)
            return cursor.fetchone()
        finally:
            conn.close()
            
    def id_mes(self, nombre_mes):
        try:
            conn = self.establecer_conexion()
            cursor = conn.cursor()
            sql = 'Select id_arriendo FROM arriendos WHERE mes = ?'
            cursor.execute(sql, nombre_mes)
            return cursor.fetchone()
        finally:
            conn.close()
        
        
    def datos_scroll(self, id_inquilino):
        try:
            
            conn = self.establecer_conexion()
            cursor = conn.cursor()
            sql = 'SELECT codigo,mes FROM inquilino_arriendo JOIN inquilinos ON inquilino_arriendo.id_inquilino = inquilinos.id_inquilino JOIN arriendos ON inquilino_arriendo.id_arriendo = arriendos.id_arriendo WHERE inquilinos.id_inquilino = ?'
            cursor.execute(sql, id_inquilino)
            return cursor.fetchall()
        finally:
            conn.close()
            
    def verificar_cobro(self, idmes_idinq):
        
        try:
            conn = self.establecer_conexion()
            cursor = conn.cursor()
            sql = 'SELECT * FROM inquilino_arriendo WHERE id_arriendo = ? AND id_inquilino = ?'
            cursor.execute(sql, idmes_idinq)
            return cursor.fetchall()
        finally:
            conn.close()
            
            
        