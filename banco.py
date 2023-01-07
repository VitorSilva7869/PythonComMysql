import sqlite3
from sqlite3 import Error
import os
import mysql.connector

"""from mysql.connector import errorcode
def conexão():
    try:
        Conexão_Banco = mysql.connector.connect(host='localhost', user='root', password='', database='senai')
        print("Database connection made!")
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("User name or password is wrong")
        else:
            print(error)
    else:
        Conexão_Banco.close()"""



#Conexão SqlLite

"""def ConexãoBanco():
    con=None
    try:
        con=sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con"""

#Funçoes

def dql(query): #select
    vcon= Conexão_Banco = mysql.connector.connect(host='localhost', user='root', password='', database='dbescola')
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def dml(query): #insert, update, delete
    try:
        con = Conexão_Banco = mysql.connector.connect(host='localhost', user='root', password='', database='dbescola')
        c=con.cursor()
        c.execute(query)
        con.commit()
        con.close()
    except Error as ex:
        print("Erro")



'''v_turma_aluno = "34"
v_cpf_aluno = "72439475"
v_nome_aluno = "Lara"        
v_id_aluno = "14"
vquery="INSERT INTO aluno(id_aluno,nome_aluno,cpf_aluno) VALUES('"+v_id_aluno+"','"+v_nome_aluno+"','"+v_cpf_aluno+"' )"
dml(vquery)'''