# class Calculadora:
#     def __init__(self,num1,num2):                         #metodo é não retorna varialvel
#         self.valor_a = num1                                 #função retorna varialvel
#         self.valor_b = num2
#
#     def soma(a, b):
#         return self.valor_a + self.valor_b
#
#     def subtracao(a, b):
#         return self.valor_a - self.valor_b
#
#     def multiplicacao(a, b):
#         return self.valor_a * self.valor_b
#
#     def divisao(a, b):
#         return self.valor_a / self.valor_b
#
# calculadora = Calculadora(10, 2)
# print(calculadora.valor_a)
# print(calculadora.soma())
# print(calculadora.subtracao())
# print(calculadora.subtracao())
# print(calculadora.divisao())

#
# class Calculadora:                               # função retorna varialvel
#     def __init__(self,):                         #metodo é não retorna varialvel
#             pass                                 #como o init não pode ficar vazio, você coloca o pass( que é para passar)
#                                                  #nesse caso não precisaria do init, mas vou deixar para fins educativos
#
#     def soma(self, valor_a, valor_b):
#         return valor_a + valor_b
#
#     def subtracao(self, valor_a, valor_b):
#         return valor_a - valor_b
#
#     def multiplicacao(self, valor_a, valor_b):
#         return valor_a * valor_b
#
#     def divisao(self, valor_a, valor_b):
#         return valor_a / valor_b
#
# calculadora = Calculadora()
# print(calculadora.soma(10,2))
# print(calculadora.subtracao(11,2))
# print(calculadora.subtracao(25,5))
# print(calculadora.divisao(100,25))


#
# class Televisao:
#     def __init__(self):
#         self.canal = 5
#         self.ligado = False
#
#     def power(self):
#         if self.ligado:
#             self.ligado = False
#         else:
#             self.ligado = True
#
#     def aumenta_canal(self):
#         self.canal += 1
#
#     def diminui_canal(self):
#         self.canal -= 1
#
# televisao = Televisao()
# print('a televisão está ligada {}'.format(televisao.ligado))
# televisao.power()
# print('a televisão está ligada {}'.format(televisao.ligado))
# print('qual é o canal da TV: {}'.format(televisao.canal))
# televisao.aumenta_canal()
# televisao.aumenta_canal()
# televisao.aumenta_canal()
# print('qual é o canal agora: {}'.format(televisao.canal))
# televisao.diminui_canal()
# televisao.diminui_canal()
# televisao.diminui_canal()
# televisao.diminui_canal()
# televisao.diminui_canal()
# televisao.diminui_canal()
# print('qual é o canal agora então: {}'.format(televisao.canal))
#
