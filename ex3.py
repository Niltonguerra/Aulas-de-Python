#fazer um programa que aceite 7 notas de jurados e pegar o maior e menor valor e a média dos demais valores

def somal(list):
    soma = 0
    for x in list:
        soma = soma+x
    soma=soma/5
    return soma

notas_juiz= [7,2,3,4,5,6,1]
notas_juiz.sort()
print('maior nota:{}'.format(notas_juiz[6]))
print('menor nota:{}'.format(notas_juiz[0]))
notas_juiz.pop()
notas_juiz.pop(0)
media= somal(notas_juiz)
print('media das notas:{}'.format(media))