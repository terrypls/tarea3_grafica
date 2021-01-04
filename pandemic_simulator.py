import sys
from view import Simulador

if len(sys.argv) > 1:
    virus = sys.argv[1]

Simulador(virus)

