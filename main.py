from uteis import dados, moeda

valor = dados.leiaDinheiro('Digite o preço R$') #850,99
# valor = dados.leiaDinheiro('Digite o preço R$') # (espaço em branco)
# valor = dados.leiaDinheiro('Digite o preço R$') #  (2 ou mais espaços em branco)
# valor = dados.leiaDinheiro('Digite o preço R$') #banana
moeda.resumo(valor, 35, 22, True)