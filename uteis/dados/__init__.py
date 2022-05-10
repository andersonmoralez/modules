def leiaDinheiro(str):
    val = input(f'{str}')

    if val == 'exit':
        return val

    if ('.' in val or ',' in val) and (val.replace('.', '').isnumeric() or val.replace(',', '').isnumeric()):
        if ',' in val:
            val = val.replace(',', '.')
        val = float(val)
        # print(val)
        return val
    elif val.isnumeric() is True:
        val = float(val)
        return val
    elif val.isalpha() is True:
        print(f'ERRO: "{val}" é um Preço invalido')
        val = False
    elif ' '.isalpha() is False:
        print(f'ERRO: "{val}" é um Preço invalido')
        val = False

    return val

