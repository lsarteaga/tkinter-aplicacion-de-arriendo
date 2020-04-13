#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:43:10 2020

@author: lsarteaga
"""
#importaciones
import sqlite3

class Logica():
    def establecer_conexion(self):
        conexion = sqlite3.connect('arriendo.db')
        return conexion
    
