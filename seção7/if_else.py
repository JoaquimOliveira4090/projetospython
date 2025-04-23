def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'menor de idade'
    elif idade in range(18, 64):
        return 'adulto'
    elif idade in range(65, 100):
        return 'me 100: int e'
    elif idade >= 100:
        return 'centenario'
    else:
        return 'idade invalida'
    
    if __name__ == '__main__':
        for idade in (17, 0, 35, 87, 113, -2):
            print(f'{idade}: {faixa_etaria(idadae)}') 