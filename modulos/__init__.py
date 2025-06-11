# -*coding: utf-8 -*-
import os
from .alarmEntry import ALARM
from .systemclock import SYSTEMCLOCK
<<<<<<< HEAD
# from .player import PLAYER
from .player_pgmixer import PLAYER
=======
from .player import PLAYER
# from .player_pgmixer import PLAYER
>>>>>>> d3281149ec38ae7a0729dc7a12305626118c1d46
from .slct_file import FILESELECTOR
from .btn import CBUTTON
from .systemdate import SYSDATE

# PARA ACTUALIZAR
# from .player_pgmixer import PLAYER
# from .cronotest import CRONO

# PARA REVISION
# from .twodigitbrick import TWODIGITBRICK
# from . import utils


#----------------------------------------------
# <<<< Esta sección funciona correctamente >>>>
# <<<< pero solo se obtienen los modulos   >>>>
# <<<< no las clases contenidas en ellos      >>>>
""" import os
import importlib

modules_list = [
    'systemclock',
    'alarmEntry',
    'player',
    'slct_file',
    'btn',
    'systemdate'
]
clas_list = [
    'SYSTEMCLOCK',
    'ALARM',
    'PLAYER',
    'FILESELECTOR',
    'CBUTTON',
    'SYSDATE',
]

def my_import(module, clas):
    pckg = (os.path.dirname(__file__)).split('\\')[-1]
    mod = importlib.import_module(name=os.curdir + module, package=pckg)
    cl = getattr(mod, clas)
    print(mod, cl)
    return mod, cl


for module, clas in zip(modules_list, clas_list):
    my_import(module, clas) """

#----------------------------------------------
# <<<< Esta sección funciona correctamente
# pero descompone la importacion desde utils >>>>
""" import os
import importlib
my_list = [
    'systemclock.SYSTEMCLOCK',
    'alarmEntry.ALARM',
    'player.PLAYER',
    'slct_file.FILESELECTOR',
    'systemdate.SYSDATE',
    'btn.CBUTTON'
]
def my_import(name):
    global cl, component
    module = name.split('.')[0]
    component = name.split('.')[1:]
    pckg = (os.path.dirname(__file__)).split('\\')[-1]
    print('1.- ' + pckg)
    mod = importlib.import_module(name=os.curdir + module, package='.' + pckg)
    for comp in component:
        cl = getattr(mod, comp)
        classes = {comp: cl}
        print('1.1.- ', mod, cl, comp, classes)
        return mod, cl, comp, classes

for mod in my_list:
    my_import(mod) """