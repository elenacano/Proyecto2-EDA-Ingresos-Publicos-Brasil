import pandas as pd

def suma(a,b):
    return a+b


def rellenar_id_os(id, nombre, dic, df):
    if dic[nombre] != id:
        print(f"El id es {id} y deberia ser {dic[nombre]}")

def rellenar_os(id, nombre, dic, df):
    if dic[id] != nombre :
        df["nombre organizacion"] = dic[id]
        

def cambio_id_39251(id):
    if id == 39251:
        return 68201
    else:
        return id
    
def cambio_id_20117(id):
    if id == 20117:
        return 30912
    else:
        return id
    
def cambio_id_64902(id):
    if id == 64902:
        return 30914
    else:
        return id
    
def cambio_id_64901(id):
    if id == 64901:
        return 30913
    else:
        return id
    
def cambio_id_130214(id):
    if id == 130214:
        return 440088
    else:
        return id
    
def cambio_id_410002(id):
    if id == 410002:
        return 240102
    else:
        return id
    
def cambio_id_873001(id):
    if id == 873001:
        return 673001
    else:
        return id
    
def cambio_id_393002(id):
    if id == 393002:
        return 682010
    else:
        return id
    
def cambio_id_110246(id):
    if id == 110246:
        return 200246
    else:
        return id
    
def cambio_id_207001(id):
    if id == 207001:
        return 307002
    else:
        return id