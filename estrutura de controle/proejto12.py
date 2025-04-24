from math import pi
import sys

class terminalcolor:
    erro = '\033[91m]'
    normal = '\033[0m]'

def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("É necessario informar o raio do circulo")
        print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))
else:
    raio = sys.argv[1]
    area = circulo(raio)
    print('area do circulo', area)