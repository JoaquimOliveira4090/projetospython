def executar(funcao):
    funcao()

def bom_dia():
    print('bom dia!')

def boa_tarde():
    print('boa tarde!')

if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)