'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
| PYEWS, ElectricalWireSizes, 20/04/2022                                 |
| Version : 0.1.27rc3                                                    |
| Autor : Marco Polo Jacome Toss                                         |
| License: GNU Affero General Public License v3 (GPL-3.0)                |
| Requires: Python >=3.5                                                 |
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Changelog:

0.1.27rc3: En esta versión los módulos se han clasificado e independizado
           en distintos archivos además se mejora la salida de datos
           del módulo dbcircuit para funciones futuras.

0.1.27:    Versione estable.

'''

'''
from .kElectric import mbtcu
from .kElectric import mbtal
from .kElectric import mbtcustd
from .kElectric import dbc
from .kElectric import Rn
from .kElectric import Z
from .kElectric import dbcircuit
from .kElectric import dbcircuitcd
from .kElectric import zpual
from .kElectric import zpucu
from .kElectric import graph
from .kElectric import version
from .kElectric import icc

'''
from .basicelecfunc import Rn, RnCd, Z, Rcd, dbc, FCT, zpucu, zpual
from .dbcircuit import dbcircuit
from .dbcircuitcd import dbcircuitcd
from .graph import autolabel, graph
from .mbtcu import mbtcu
from .mbtal import mbtal
from .mbtcustd import mbtcustd
from .shortcircuit import icc
from .version import version
