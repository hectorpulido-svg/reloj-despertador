from cx_Freeze import setup, Executable
import sys
import os
import distutils

'''
    dentro de la carpeta que contiene el archivo .py a compilar
    ejecutar en la terminal como administrador el comando
    -- python Mi_setup.py build --
'''

os.environ['TCL_LIBRARY'] = 'C:\\Python39\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'C:\\Python39\\tcl\\tk8.6'

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('G:\\python\\simples_practicas\\reloj-despertador\\main.py', base=base)
]

setup(name='reloj despertador',
      version='0.1',
      options={'build.exe': {'packages': [], 'include_files': [], 'excludes': []}},
      description='simple reloj despertador para windows',
      executables=executables
      )