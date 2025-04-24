def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    assert tag_bloco('incluido com sucesso!') == \
        '<div class="success">Incluido com sucesso!</div>'
    assert tag_bloco('impossivel excluir!', 'error') == \
        '<div class="error">impossivel excluir!</div>'
    print(tag_bloco('bloco'))