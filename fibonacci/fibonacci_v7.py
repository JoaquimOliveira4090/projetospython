def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
        return resultado 
        

if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib)