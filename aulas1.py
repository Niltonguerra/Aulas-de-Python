# aula02
# a,b = 10,10
# soma = a+b
# subtracao = a-b
# multiplicacao = a*b
# divicao = a/b
# resto= a%b
#
# ironman = 1000*10000
# print('eu amo você mais de {}'.format(ironman))
#
# ab = int(input('soma:'))
# ba = int(input('soma:'))


# # Aula03
# a = int(input('primeiro valor:'))
# b = int(input('segundo valor:'))
# c = int(input('terceiro valor:'))
# if a > b:
#     print('o maior numero é {}.'.format(a))
# elif b > a and b > c:
#     print('o maior número é {}.'.format(b))
# else:
#     print('o maior número é {}'.format(c))
# print('final do programa') #está fora do ''if'

# a = int(input('entre com um valor:'))
# b = int(input('entre com um valor:'))
# restoa = a % 2
# restob = a % 2
#
# if restoa == 0 or not restob > 0:
#     print('foi digitado um número par')
# else:
#     print('nenhum é número par')

primeiro = int(input('nota do primeiro bimestre:'))
while primeiro >= 10:
    primeiro = int(input('nota errada, por favor insira novamente:'))

segundo = int(input('nota do segundo bimestre'))
while segundo >= 10:
    segundo = int(input('nota errada, por favor insira novamente:'))

terceiro = int(input('nota do terceito bimestre'))
while terceiro >= 10:
    terceiro = int(input('nota errada, por favor insira novamente:'))

quarto = int(input('nota do quarto bimestre'))
while quarto >= 10:
    quarto = int(input('nota errada, por favor insira novamente:'))

while primeiro >= 10:
    quarto = input('nota errada, por favor insira novamente:')

media = (primeiro+segundo+terceiro+quarto)/4

if media >= 5 and primeiro <= 10 and segundo <= 10 and terceiro <= 10 and quarto <= 10:
    print('Ele passou de ano, sua nota é {}'.format(media))

else:
    print('ele não passou de ano, sua nota é: {}'.format(media))



#Aula04

# num = int(input('entre com um número:'))
#
# for i in range (num):
#     div = 0
#     for x in range(1, i+1):
#         resto = i % x
#         if resto == 0:
#             div += 1
#     if div > 2:
#             print('esse número não é primo')
#     else:
#             print('esse número é primo')

# a = 0
# while a <= 10:
#     print(a)
#     a +=1
