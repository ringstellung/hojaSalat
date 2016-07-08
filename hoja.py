# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

if __name__ == "__main__":
    from horario import *
    z = mesTxtToLaTeX(sys.argv[1],int(sys.argv[3]),int(sys.argv[4]))
    from relleno import *
    rellenoPlant(sys.argv[1],
                 int(sys.argv[2]),
                 int(sys.argv[3]),
                 z)

