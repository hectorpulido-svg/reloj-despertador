from cx_Freeze import setup, Executable
import sys
import os
cwd = os.getcwd()
import distutils

'''
    dentro de la carpeta que contiene el archivo .py a compilar
    ejecutar en la terminal como administrador el comando
    -- python Mi_setup.py build --
'''
# C:\Users\hemip\AppData\Local\Programs\Python\Python310
os.environ['TCL_LIBRARY'] = 'C:\\Users\hemip\\AppData\Local\\Programs\\Python\\Python310\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'C:\\Users\hemip\\AppData\Local\\Programs\\Python\\Python310\\tcl\\tk8.6'

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable(os.path.join(cwd, 'relojDespertador.py'), icon=os.path.join(cwd, '\\img\\icon\\TimeAlarmclock.ico'), base=base)
]
# executables = [
#     Executable('E:\\Python\\reloj-despertador\\relojDespertador.py', icon='E:\\Python\\reloj-despertador\\img\\icon\\TimeAlarmclock.ico', base=base)
# ]

setup(name='reloj despertador',
      version='1.0',
      options={'build.exe': {'packages': [], 'include_files': [], 'excludes': []}},
      description='simple reloj despertador para windows',
      executables=executables
      )