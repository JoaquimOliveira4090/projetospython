with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome {}, idade: {}'.format(*pessoa), file=saida)


if arquivo.closed:
    print("Arquivo ja foi fechado!")

if saida.closed:
    print('arquivo de saida ja foi fechado')
