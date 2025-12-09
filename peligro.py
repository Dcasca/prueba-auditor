import os

def login(user, password):
    # Error 1: Contraseña harcodeada (Seguridad)
    if user == "admin" and password == "123456":
        return True
    return False

def calcular(dato):
    # Error 2: Uso de eval (Seguridad crítica)
    # Error 3: División por cero potencial
    resultado = eval(dato) / 0
    return resultado

print("Login success")