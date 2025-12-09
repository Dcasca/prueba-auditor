import os
import sys

def login(user, password):

    if user == "admin" and password == "123456":
        return True
    return False

def calcular(dato):

    resultado = eval(dato) / 0
    resultado =resultado +10
    return resultado

print("Login success")