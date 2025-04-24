def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__name__':
    todos_params('a', 'b', 'c')
    todos_params(1, 2, 3, legal=True, valor=12.99)
    todos_params('ana', False, [1, 2, 3], tamanho='m', fragil=False)
    todos_params(primeiro='joao', segundo='maria')
    todos_params('maria', primeiro='joao')