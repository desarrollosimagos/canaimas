# -*- encoding: utf-8 -*-
from PIL import Image
import os
def dictfetchall(cursor):
    """
    Metodo global para recorrer con el objeto dictfetchall (Clave Valor)
    """
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

# METODOS GLOBALES
######################################################################
def acento(cadena):
	result = cadena.encode('UTF-8').decode('UTF-8') # INSTITUCION
	return result
#####################################################################
# Metodo global para fechas
def fecha(fecha):
	date = fecha.split("-")
	nueva_fecha = date[2]+"/"+date[1]+"/"+date[0]
	return nueva_fecha
#####################################################################
# Metodo global para redondear cifras
def decimal(cadena):
	salida = "%.2f" % round(cadena,2)
	return salida

# Formatear cadena

def f_string(s):

    if s == "1":
        s = "SI"
    else:
        s = "NO"
    return s

# Metodo que permite redimencionar la imagen (94 * 124)
def save_image(foto):

    os.path.dirname(os.path.abspath(__file__))
    DIR_URL = os.getcwd()

    nameimg = DIR_URL+str('/foto/')+str(foto)
    imagpath = nameimg
    imag = Image.open (imagpath,mode='r')
    imag = imag.resize((94, 124), Image.ANTIALIAS)
    imag.save(nameimg)

