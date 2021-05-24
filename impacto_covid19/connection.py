# -*- coding: utf-8 -*-
"""
Created on Tue May 18 08:07:07 2021

@author: ximen
"""
import psycopg2

class Connection:
    
    def __init__(self):
        self.connection = None
    
    def openConnection(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="13042",
                                               database="peajes",
                                               host="localhost", 
                                               port="5432")
        except Exception as e:
            print (e)

    def closeConnection(self):
        self.connection.close()