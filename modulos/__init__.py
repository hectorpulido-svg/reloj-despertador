# -*coding: utf-8 -*-

from .alarmEntry import ALARM
from .systemclock import SYSTEMCLOCK
from .player import PLAYER
from .slct_file import FILESELECTOR
from .btn import CBUTTON
from .systemdate import SYSDATE
# from .cronotest import CRONO
# from .twodigitbrick import TWODIGITBRICK
# from . import utils


#----------------------------------------------
# <<<< Esta sección funciona correctamente >>>>
# <<<< pero solo se obtienen los modulos   >>>>
# <<<< no la clase contenida en ellos      >>>>
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
# <<<< Esta sección funciona correctamente >>>>
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
    print(pckg)
    mod = importlib.import_module(name=os.curdir + module, package='.' + pckg)
    for comp in component:
        cl = getattr(mod, comp)
        classes = {comp: cl}
        print(mod, cl, comp, classes)
        return mod, cl, comp, classes

for mod in my_list:
    my_import(mod) """