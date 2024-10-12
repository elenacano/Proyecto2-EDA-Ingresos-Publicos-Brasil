import pandas as pd

def suma(a,b):
    return a+b


def rellenar_id_os(id, nombre, dic, df):
    if dic[nombre] != id:
        print(f"El id es {id} y deberia ser {dic[nombre]}")

def rellenar_os(id, nombre, dic, df):
    if dic[id] != nombre :
        df["nombre organizacion"] = dic[id]
        
