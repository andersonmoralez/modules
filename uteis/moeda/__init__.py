import locale

locale.setlocale(locale.LC_MONETARY, 'pt_br.UTF-8')

def fatorial(num):
    fat = 1
    for aux in range(1, num+1):
        fat *= aux
    return fat

def porcentagem(porc, val):
    porc = (porc/100)*val
    return porc

def moeda(val):
    val = locale.currency(val)
    return val

def resumo(prec, aum, red, real):
    if real is True:
        return print(f'\n Preço analisado: {prec}'
                     f'\n Dobro do preço: {dobro(prec, True)}'
                     f'\n Metade do preço: {metade(prec, True)}'
                     f'\n {aum}% de aumento: {aumentar(prec, aum, True)}'
                     f'\n {red}% de redução: {diminuir(prec, red, True)}')
    else:
        return print(f'\n Preço analisado: {prec}'
                     f'\n Dobro do preço: {dobro(prec, False)}'
                     f'\n Metade do preço: {metade(prec, False)}'
                     f'\n 80% de aumento: {aumentar(prec, aum, False)}'
                     f'\n 35% de redução: {diminuir(prec, red, False)}')

def aumentar(n, v, real):
    if n is False:
        exit()
    else:
        porc = porcentagem(n, v)
        n = n + porc

        if real is True:
            return moeda(n)
        else:
            return n

def diminuir(n, v, real):
    if n is False:
        exit()
    else:
        porc = porcentagem(n, v)
        n = n - porc

        if real is True:
            return moeda(n)
        else:
            return n

def dobro(n, real):
    if n is False:
        exit()
    else:
        n = n*2

        if real is True:
            return moeda(n)
        else:
            return n

def metade(n, real):
    if n is False:
        exit()
    else:
        n = n/2

        if real is True:
            return moeda(n)
        else:
            return n