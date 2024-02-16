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

os.environ['TCL_LIBRARY'] = 'C:\\Python39\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'C:\\Python39\\tcl\\tk8.6'

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable(os.path.join(cwd, 'reloj-despertador.py'), icon=os.path.join(cwd, '\\img\\icon\\TimeAlarmclock.ico'), base=base)
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