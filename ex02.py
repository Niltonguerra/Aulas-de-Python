
# calcular o raio de um circulo
# raio = int(input('escreva o número do raio:'))
# aréa = raio*raio*3.1415
# # print ('a aréa do circuito é: {}'.format(aréa))



# transformador de celsius para fahrenheit e vise versa
# escolha = (input(('qual é a temperatura em fahrenheit? \n a)sim   b)não')))
# if escolha == 'a':
#     f = int(input(('qual é a temperatura em fahrenheit?')))
#     c= 5 * ((f-32) / 9)
#     print('a temperatura equivalente disso em Celsius é: {}'.format(c))
# if escolha == 'b':
#     cel = int(input(('qual é a temperatura em Celsius?')))
#     far= ((cel *9)/5)+32
#     print('a temperatura equivalente disso em fahrenheit é: {}'.format(far))



# programa para calcular quanto de parede você quer pintar
# # math.floor() arredonda para baixo
# # math.ceil() arredonda para cima
# quant =int(input('quantos metros você gostaria de pintar?'))
#
# a =math.ceil(quant/108)*80
#
# b =math.ceil(quant/21.6)*25
#
# lata = math.floor(quant/108)
# galoes =math.ceil((quant%108)/21.6)
# v_galoes = galoes*25
# v_lata = lata*80
# valor_mais_barato = v_lata+v_galoes
#
# print('você tem a opição de comprar apenas latas, isso custa: {}\n'
#       'você tem a opição de comprar apenas galões, isso custa: {}\n'
#       'e você tem a opição mais barata, que é:{} \n'.format(a,b, valor_mais_barato))


consoante = []
p = input('digite uma palavra:')
for letra in p:
    if letra in 'b, c, d, f, g, h, j, k, l,1, m, n, p, q, r, s, t, v, x, y, w, z':
        consoante.append(letra)
print('sua palavra é {}, e ela tem as consoantes : {}'.format(p, consoante))
