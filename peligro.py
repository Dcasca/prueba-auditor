import os
import sys

def login(user, password):

    if user == "admin" and password == "123456":
        return True
    return False

def calcular(dato):

    resultado = eval(dato) / 0
    resultado =resultado +30
    return resultado

def dividir(dato):

    resultado = dato / 12
    resultado =resultado +30
    return resultado
print("Login success")