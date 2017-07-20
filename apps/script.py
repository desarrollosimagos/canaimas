# FECHA: 30 de Junio 2015
import sys
import os
from os import listdir
from os.path import isfile, join

"""
    Metodo global para ubicar de forma automatica en el directorio
    y a su vez borrar los archivos internos
"""
def delete_Files(folder):
      files_dump = [join(folder, c) for c in listdir(folder)]
      files_dump = filter(lambda c: isfile(c), files_dump)
      [os.remove(c) for c in files_dump]