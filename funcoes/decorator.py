def log(function):
    def decorator(*args, **kwargs):
        print(f'inicio da chamada da função: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y

@log
def sub(x, y):
    return x - y

if __name__ == '__main__':
    print(soma(5, 7))
    print(sub(5, y=7))