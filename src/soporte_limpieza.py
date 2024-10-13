import json
import pandas as pd

def suma(a,b):
    return a+b


def rellenar_id_os(id, nombre, dic, df):
    if dic[nombre] != id:
        print(f"El id es {id} y deberia ser {dic[nombre]}")

def rellenar_os(id, nombre, dic, df):
    if dic[id] != nombre :
        df["nombre organizacion"] = dic[id]

# def rellenar_orga_sup(row):
#     with open('../datos/diccionario_orga_a_sup.json', 'r') as file:
#         diccionario_orga_a_sup = json.load(file)
#     # Accedemos a los nulos que etán donde ambos campos son nulos.
#     if pd.isna(row['id organizacion superior']) and pd.isna(row['organizacion superior']):
#         id_org = row['id organizacion']
#         if id_org in diccionario_orga_a_sup:
#             row['id organizacion superior'], row['organizacion superior'] = diccionario_orga_a_sup[id_org]
#     return row       

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