from tabulate import tabulate
from .bd import dbConductorCu, dbConductorAl, dbConductorCuStd
from .basicelecfunc import Rn, RnCd, Z, Rcd, dbc, FCT, zpucu, zpual
from .mbtcu import mbtcu
from .mbtal import mbtal
from .mbtcustd import mbtcustd
from .dbcircuit import dbcircuit
from .dbcircuitcd import dbcircuitcd
from .graph import autolabel, graph
from .shortcircuit import icc

import numpy as np
import matplotlib.pyplot as plt
import math
import time


'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
| PYEWS, ElectricalWireSizes, 02/06/2022                                 |
| Version : 0.1.28                                                       |
| Autor : Marco Polo Jacome Toss                                         |
| License: GNU Affero General Public License v3 (GPL-3.0)                |
| Requires: Python >=3.5                                                 |
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Changelog:

0.1.28   : Versión estable.

0.1.28rc2: Separación de operaciones, conductor y protección.

0.1.28rc1: En esta versión se actualiza las protecciones y se actualiza
           la fórmula de corriente incluyendo el factor de sobrecorriente,
           en la versión 0.1.27 no se logra ver la actualización de la
           corriente nominal.

0.1.27rc3: En esta versión los módulos se han clasificado e independizado
           en distintos archivos además se mejora la salida de datos
           del módulo dbcircuit para funciones futuras.

0.1.27:    Versione estable.

'''


def version():
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("                                                                          ")
    print("                         ─▄▀─▄▀")
    print("                         ──▀──▀")
    print("                         █▀▀▀▀▀█▄")
    print("                         █░░░░░█─█")
    print("                         ▀▄▄▄▄▄▀▀")
    print("                                                                          ")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("| Python ElectricalWireSizes, 15/06/2022                                 |")
    print("| Version : 0.1.28                                                       |")
    print("| Autor : Marco Polo Jacome Toss                                         |")
    print("| License: GNU Affero General Public License v3 (GPL-3.0)                |")
    print("| Requires: Python >=3.5                                                 |")
    print("| PyPi : https://pypi.org/project/ElectricalWireSizes/                   |")
    print("| Donativos : https://ko-fi.com/jacometoss                               |")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")  

    


