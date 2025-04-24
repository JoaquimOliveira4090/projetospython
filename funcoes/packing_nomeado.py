def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')

if __name__ == '__main__':
    resultado_f1(primeiro='l. hamilton',
                 segundo='m, verstappen',
                 terceiro='s. vettel')
    